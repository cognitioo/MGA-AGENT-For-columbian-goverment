"""
MGA AI Agent - Streamlit Web Interface
Herramienta de apoyo para formulación de proyectos públicos en la plataforma MGA del DNP

Features:
- Multi-model support (Groq, Gemini, OpenAI, Anthropic)
- Document generation for Estudios Previos and Análisis del Sector
- Word document download
- Spanish language interface
"""
 
import streamlit as st
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import get_llm, get_available_providers, LLM_PROVIDERS, APP_TITLE, APP_DESCRIPTION
from generators.estudios_previos_generator import EstudiosPreviosGenerator
from generators.analisis_sector_generator import AnalisisSectorGenerator
from generators.dts_generator import DTSGenerator
from generators.certificaciones_generator import CertificacionesGenerator
from generators.mga_subsidios_generator import MGASubsidiosGenerator
from generators.docx_builder import DocumentBuilder
from extractors.document_data_extractor import extract_data_from_upload
from generators.unified_generator import UnifiedGenerator


# --- Page Configuration ---
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Professional Look ---
st.markdown("""
<style>
    /* Main styling */
    .main-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 0.3rem;
    }
    .sub-header {
        font-size: 0.95rem;
        color: #555;
        margin-bottom: 1.5rem;
    }
    .section-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a2e;
        border-left: 3px solid #4CAF50;
        padding-left: 0.8rem;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    
    /* Model badge */
    .model-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 2px;
    }
    .model-groq { background: #f0f4ff; color: #3b5998; border: 1px solid #3b5998; }
    .model-gemini { background: #fff3e0; color: #e65100; border: 1px solid #e65100; }
    .model-openai { background: #e8f5e9; color: #2e7d32; border: 1px solid #2e7d32; }
    .model-anthropic { background: #fce4ec; color: #c2185b; border: 1px solid #c2185b; }
    
    /* Success/info boxes */
    .success-box {
        background-color: #e8f5e9;
        border-left: 4px solid #4CAF50;
        border-radius: 4px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #e3f2fd;
        border-left: 4px solid #2196F3;
        border-radius: 4px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Sidebar styling */
    .sidebar-section {
        padding: 0.5rem 0;
        border-bottom: 1px solid #eee;
        margin-bottom: 0.5rem;
    }
    .sidebar-title {
        font-weight: 600;
        color: #333;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = None
if 'generated_file' not in st.session_state:
    st.session_state.generated_file = None
if 'extracted_data' not in st.session_state:
    st.session_state.extracted_data = {}


def render_data_upload_option(doc_type: str, key_prefix: str) -> dict:
    """
    Render the data file upload option for auto-filling forms
    
    Args:
        doc_type: Document type for extraction mapping
        key_prefix: Unique key prefix for Streamlit widgets
        
    Returns:
        Dictionary with extracted data (empty if none)
    """
    with st.expander("📄 Cargar archivo con datos del proyecto (opcional)", expanded=False):
        st.info("Suba un archivo PDF, DOCX o XLSX con información del proyecto para auto-llenar el formulario.")
        
        data_file = st.file_uploader(
            "Archivo de datos",
            type=["pdf", "docx", "xlsx"],
            key=f"{key_prefix}_data_file",
            help="El sistema extraerá automáticamente los datos del proyecto"
        )
        
        if data_file:
            if st.button("🔍 Extraer Datos", key=f"{key_prefix}_extract_btn"):
                with st.spinner("Extrayendo datos del documento..."):
                    try:
                        # Get LLM for AI extraction if available
                        model = st.session_state.get('selected_model', 'groq')
                        try:
                            llm = get_llm(model)
                        except:
                            llm = None
                        
                        extracted = extract_data_from_upload(data_file, doc_type, llm)
                        
                        if extracted and not extracted.get("error"):
                            st.session_state.extracted_data[doc_type] = extracted
                            st.success(f"✅ Se extrajeron {len(extracted)} campos del documento")
                            
                            # Show extracted data
                            with st.expander("Ver datos extraídos", expanded=True):
                                for field, value in extracted.items():
                                    st.text(f"{field}: {value[:100]}..." if len(str(value)) > 100 else f"{field}: {value}")
                        else:
                            st.warning("No se pudieron extraer datos del documento. Complete el formulario manualmente.")
                    except Exception as e:
                        st.error(f"Error al extraer datos: {str(e)}")
    
    return st.session_state.extracted_data.get(doc_type, {})


def get_model_options():
    """Get available model options based on configured API keys"""
    options = {}
    
    # Check for Groq (priority)
    if os.getenv("GROQ_API_KEY"):
        options["groq"] = "Groq - Llama (Rápido)"
    
    # Check for Gemini
    if os.getenv("GOOGLE_API_KEY"):
        options["gemini"] = "Google Gemini"
    
    # Check for OpenAI
    if os.getenv("OPENAI_API_KEY"):
        options["openai"] = "OpenAI GPT-4"
    
    # Check for Anthropic
    if os.getenv("ANTHROPIC_API_KEY"):
        options["anthropic"] = "Anthropic Claude"
    
    if not options:
        options["groq"] = "Groq (Configure API Key)"
    
    return options


def render_sidebar():
    """Render the sidebar with model selection, mode, and customization controls"""
    with st.sidebar:
        # Logo/Title
        st.markdown("### 🛠️ MGA Agent")
        st.caption("Generador de Documentos")
        st.markdown("---")
        
        # ══════════════════════════════════════
        # MODE SELECTION
        # ══════════════════════════════════════
        st.markdown("**📋 Modo de Generación**")
        
        generation_mode = st.radio(
            "Seleccione modo:",
            options=["crear_nuevo", "actualizar_existente"],
            format_func=lambda x: "Crear desde cero" if x == "crear_nuevo" else "Actualizar existente",
            help="Crear nuevo: Genera documento completo con datos POAI. Actualizar: Modifica documento existente.",
            label_visibility="collapsed"
        )
        st.session_state.generation_mode = generation_mode
        
        # Upload previous document for update mode
        if generation_mode == "actualizar_existente":
            st.caption("📄 Documento base (opcional):")
            prev_doc = st.file_uploader(
                "Subir MGA anterior",
                type=["pdf", "docx"],
                help="Suba el MGA o documento del año anterior para extraer datos base",
                key="prev_doc_upload",
                label_visibility="collapsed"
            )
            if prev_doc:
                st.success(f"✓ {prev_doc.name}")
                st.session_state.previous_document = prev_doc
            
            # Edit instructions - what to change
            st.caption("✏️ ¿Qué desea modificar?")
            edit_instructions = st.text_area(
                "Instrucciones de edición",
                placeholder="Describa los cambios a realizar:\n• Actualizar valores del POAI 2025\n• Cambiar fechas a enero 2026\n• Modificar el responsable\n• Actualizar tabla de presupuesto",
                height=100,
                help="Indique al agente qué datos actualizar o modificar del documento anterior",
                key="edit_instructions",
                label_visibility="collapsed"
            )
            st.session_state.edit_instructions = edit_instructions
        
        st.markdown("---")
        
        # ══════════════════════════════════════
        # MODEL SELECTION
        # ══════════════════════════════════════
        st.markdown("**🤖 Modelo de IA**")
        
        model_options = get_model_options()
        selected_model = st.selectbox(
            "Modelo",
            options=list(model_options.keys()),
            format_func=lambda x: model_options[x],
            help="Seleccione el modelo de IA",
            label_visibility="collapsed"
        )
        
        if selected_model in LLM_PROVIDERS:
            model_info = LLM_PROVIDERS[selected_model]
            st.caption(f"Usando: {model_info['model']}")
        
        st.markdown("---")
        
        # ══════════════════════════════════════
        # TEMPLATE SELECTOR
        # ══════════════════════════════════════
        st.markdown("**📑 Plantilla de Estructura**")
        
        template = st.selectbox(
            "Plantilla",
            options=["estandar", "simplificado", "completo", "personalizado"],
            format_func=lambda x: {
                "estandar": "Estándar",
                "simplificado": "Simplificado (menos secciones)",
                "completo": "Completo (todas las secciones)",
                "personalizado": "Personalizado"
            }.get(x, x),
            help="Seleccione una plantilla predefinida o personalice",
            label_visibility="collapsed"
        )
        st.session_state.selected_template = template
        
        st.markdown("---")
        
        # ══════════════════════════════════════
        # SECTION TOGGLES (for Análisis del Sector)
        # ══════════════════════════════════════
        with st.expander("📊 Secciones Activas", expanded=False):
            st.caption("Marque las secciones a incluir:")
            
            # Initialize section toggles in session state
            if 'section_toggles' not in st.session_state:
                st.session_state.section_toggles = {
                    "objeto": True,
                    "alcance": True,
                    "descripcion_necesidad": True,
                    "introduccion": True,
                    "definiciones": True,
                    "desarrollo_estudio": True,
                    "analisis_sector": True,
                    "grafico_pib": True,
                    "tabla_smlmv": True,
                    "riesgos": True,
                    "estudios_contratacion": True,
                    "recomendaciones": True,
                    "fuentes": True,
                    "estimacion_valor": True,
                }
            
            # Apply template presets
            if template == "simplificado":
                preset = {"objeto": True, "alcance": True, "descripcion_necesidad": True, 
                         "riesgos": True, "estimacion_valor": True}
                for key in st.session_state.section_toggles:
                    st.session_state.section_toggles[key] = preset.get(key, False)
            elif template == "completo":
                for key in st.session_state.section_toggles:
                    st.session_state.section_toggles[key] = True
            
            # Render checkboxes
            col1, col2 = st.columns(2)
            
            with col1:
                st.session_state.section_toggles["objeto"] = st.checkbox(
                    "OBJETO", value=st.session_state.section_toggles.get("objeto", True), key="cb_objeto")
                st.session_state.section_toggles["alcance"] = st.checkbox(
                    "ALCANCE", value=st.session_state.section_toggles.get("alcance", True), key="cb_alcance")
                st.session_state.section_toggles["descripcion_necesidad"] = st.checkbox(
                    "Necesidad", value=st.session_state.section_toggles.get("descripcion_necesidad", True), key="cb_necesidad")
                st.session_state.section_toggles["introduccion"] = st.checkbox(
                    "Introducción", value=st.session_state.section_toggles.get("introduccion", True), key="cb_intro")
                st.session_state.section_toggles["definiciones"] = st.checkbox(
                    "Definiciones", value=st.session_state.section_toggles.get("definiciones", True), key="cb_def")
                st.session_state.section_toggles["desarrollo_estudio"] = st.checkbox(
                    "1. Desarrollo", value=st.session_state.section_toggles.get("desarrollo_estudio", True), key="cb_desarrollo")
                st.session_state.section_toggles["analisis_sector"] = st.checkbox(
                    "1.5 Análisis", value=st.session_state.section_toggles.get("analisis_sector", True), key="cb_analisis")
            
            with col2:
                st.session_state.section_toggles["grafico_pib"] = st.checkbox(
                    "Gráfico PIB", value=st.session_state.section_toggles.get("grafico_pib", True), key="cb_pib")
                st.session_state.section_toggles["tabla_smlmv"] = st.checkbox(
                    "Tabla SMLMV", value=st.session_state.section_toggles.get("tabla_smlmv", True), key="cb_smlmv")
                st.session_state.section_toggles["riesgos"] = st.checkbox(
                    "Riesgos", value=st.session_state.section_toggles.get("riesgos", True), key="cb_riesgos")
                st.session_state.section_toggles["estudios_contratacion"] = st.checkbox(
                    "2. Contratación", value=st.session_state.section_toggles.get("estudios_contratacion", True), key="cb_contrat")
                st.session_state.section_toggles["recomendaciones"] = st.checkbox(
                    "Recomendaciones", value=st.session_state.section_toggles.get("recomendaciones", True), key="cb_recom")
                st.session_state.section_toggles["fuentes"] = st.checkbox(
                    "Fuentes", value=st.session_state.section_toggles.get("fuentes", True), key="cb_fuentes")
                st.session_state.section_toggles["estimacion_valor"] = st.checkbox(
                    "Estimación $", value=st.session_state.section_toggles.get("estimacion_valor", True), key="cb_estim")
        
        st.markdown("---")
        
        # ══════════════════════════════════════
        # INFO SECTION
        # ══════════════════════════════════════
        st.markdown("**📚 Documentos**")
        st.markdown("""
        - Estudios Previos
        - Análisis del Sector
        """)
        
        st.markdown("---")
        st.caption("Versión 1.1 | © 2026")
        st.caption("🇨🇴 Metodología MGA - DNP")
        
        return selected_model


def render_estudios_previos_form():
    """Render input form for Estudios Previos"""
    
    # Data extraction option
    extracted = render_data_upload_option("estudios_previos", "ep")
    
    st.markdown('<p class="section-header">Datos del Proyecto</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        municipio = st.text_input("Municipio *", value=extracted.get("municipio", ""), placeholder="Ej: San Pablo")
        departamento = st.text_input("Departamento *", value=extracted.get("departamento", ""), placeholder="Ej: Bolívar")
        entidad = st.text_input("Entidad Contratante", value=extracted.get("entidad", ""), placeholder="Ej: Alcaldía Municipal")
        bpin = st.text_input("Código BPIN", placeholder="Ej: 2024000001367")
    
    with col2:
        tipo_proyecto = st.text_input("Tipo de Proyecto *", placeholder="Ej: Convenio Interadministrativo")
        valor_total = st.text_input("Valor Total (COP) *", value=extracted.get("presupuesto", ""), placeholder="Ej: 70000000")
        plazo = st.number_input("Plazo de Ejecución (días)", min_value=1, value=90)
        fuente = st.text_input("Fuente de Financiación", placeholder="Ej: Recursos Propios")
    
    st.markdown('<p class="section-header">Descripción del Proyecto</p>', unsafe_allow_html=True)
    
    necesidad = st.text_area(
        "Descripción de la Necesidad *",
        placeholder="Describa el problema o necesidad que origina el proyecto...",
        height=100
    )
    
    objeto = st.text_area(
        "Objeto del Convenio/Contrato *",
        placeholder="Describa el objeto del contrato...",
        height=80
    )
    
    alcance = st.text_area(
        "Alcance y Actividades",
        placeholder="Liste las actividades principales a desarrollar...",
        height=100
    )
    
    st.markdown('<p class="section-header">Presupuesto</p>', unsafe_allow_html=True)
    
    rubros = st.text_area(
        "Rubros Presupuestales",
        placeholder="Ej:\n- Honorarios profesionales: $50,000,000\n- Gastos operativos: $10,000,000\n- Otros: $10,000,000",
        height=100
    )
    
    st.markdown('<p class="section-header">Obligaciones (Secciones 4 y 5)</p>', unsafe_allow_html=True)
    
    obligaciones_municipio = st.text_area(
        "Obligaciones del Municipio *",
        placeholder="Liste las obligaciones del municipio. Use • para viñetas.\nEj:\n• Proveer la información cartográfica requerida\n• Facilitar el acceso del equipo técnico\n• Garantizar la disponibilidad presupuestal",
        height=120
    )
    
    obligaciones_contratista = st.text_area(
        "Obligaciones del Contratista/Empresa *",
        placeholder="Liste las obligaciones del contratista. Use • para viñetas.\nEj:\n• Ejecutar las actividades descritas en el alcance\n• Presentar informes técnicos parciales y finales\n• Cumplir con las normas de seguridad",
        height=120
    )
    
    st.markdown('<p class="section-header">CDP - Certificado de Disponibilidad Presupuestal (Sección 7)</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        cdp_codigo = st.text_input("Código CDP", placeholder="Ej: 20260108-3")
        cdp_rubro = st.text_input("Rubro", placeholder="Ej: 2.3.2.02.02.009.45.25 – Servicio de Asistencia Técnica")
    with col2:
        cdp_fecha = st.text_input("Fecha CDP", placeholder="Ej: 08/01/2026")
        cdp_fuente = st.text_input("Fuente", placeholder="Ej: SGP – Propósito General – Libre Inversión")
    with col3:
        cdp_valor = st.text_input("Valor CDP", placeholder="Ej: $17.400.000,00")
    
    st.markdown('<p class="section-header">Membrete/Letterhead</p>', unsafe_allow_html=True)
    
    letterhead_file = st.file_uploader(
        "Subir plantilla con membrete (.docx)",
        type=["docx"],
        help="Suba un archivo .docx con el encabezado y pie de página de la alcaldía. El documento generado usará este membrete."
    )
    
    st.markdown('<p class="section-header">Responsable (Sección 12)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        responsable = st.text_input("Nombre del Responsable *", placeholder="Ej: Carlos Augusto Gil Delgado")
    with col2:
        cargo = st.text_input("Cargo", value="Secretario de Planeación Municipal")
    
    return {
        "municipio": municipio,
        "departamento": departamento,
        "entidad": entidad,
        "bpin": bpin,
        "tipo_proyecto": tipo_proyecto,
        "valor_total": valor_total,
        "plazo": str(plazo),
        "fuente_financiacion": fuente,
        "necesidad": necesidad,
        "objeto": objeto,
        "alcance": alcance,
        "rubros": rubros,
        "obligaciones_municipio": obligaciones_municipio,
        "obligaciones_contratista": obligaciones_contratista,
        "responsable": responsable,
        "cargo": cargo,
        "lugar": f"Municipio de {municipio}, {departamento}",
        "cdp_data": {
            "cdp": cdp_codigo,
            "fecha": cdp_fecha,
            "rubro": cdp_rubro,
            "fuente": cdp_fuente,
            "valor": cdp_valor
        },
        "letterhead_file": letterhead_file
    }


def render_analisis_sector_form():
    """Render input form for Análisis del Sector"""
    
    # Data extraction option
    extracted = render_data_upload_option("analisis_sector", "as")
    
    st.markdown('<p class="section-header">Datos del Contrato</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        numero_contrato = st.text_input("Número de Contrato", placeholder="Ej: 001-2025")
        modalidad = st.selectbox("Modalidad", [
            "Convenio Interadministrativo",
            "Contratación Directa",
            "Licitación Pública",
            "Selección Abreviada",
            "Concurso de Méritos"
        ])
        municipio = st.text_input("Municipio *", placeholder="Ej: San Pablo")
        departamento = st.text_input("Departamento *", placeholder="Ej: Bolívar")
    
    with col2:
        entidad = st.text_input("Entidad *", placeholder="Ej: Alcaldía Municipal")
        nombre_proyecto = st.text_input("Nombre del Proyecto *", placeholder="Ej: Actualización PSMV")
        bpin = st.text_input("Código BPIN", placeholder="Ej: 2024000001367")
        valor_total = st.text_input("Valor Total (COP) *", placeholder="Ej: 70000000")
    
    st.markdown('<p class="section-header">Información del Sector</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        sector = st.text_input("Sector *", placeholder="Ej: Saneamiento Básico, Agua Potable")
        codigo_ciiu = st.text_input("Código CIIU", placeholder="Ej: 7110 - Actividades de arquitectura e ingeniería")
    
    with col2:
        codigos_unspsc = st.text_input("Códigos UNSPSC", placeholder="Ej: 77101600, 77101700")
        duracion = st.number_input("Duración (días)", min_value=1, value=90)
    
    objeto = st.text_area(
        "Objeto del Contrato *",
        placeholder="Describa el objeto del contrato...",
        height=80
    )
    
    plan_desarrollo = st.text_input(
        "Plan de Desarrollo Relacionado",
        placeholder="Ej: Plan de Desarrollo Municipal 2024-2027 'San Pablo Mejor'"
    )
    
    fuente = st.text_input("Fuente de Financiación", placeholder="Ej: Recursos Propios del Municipio")
    
    st.markdown('<p class="section-header">Responsable</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        responsable = st.text_input("Nombre del Responsable *", placeholder="Ej: Carlos Augusto Gil Delgado")
    with col2:
        cargo = st.text_input("Cargo", value="Secretario de Planeación Municipal")
    
    st.markdown('<p class="section-header">Membrete/Letterhead</p>', unsafe_allow_html=True)
    
    letterhead_file = st.file_uploader(
        "Subir plantilla con membrete (.docx)",
        type=["docx"],
        help="Suba un archivo .docx con el encabezado y pie de página de la alcaldía.",
        key="analisis_letterhead"
    )
    
    return {
        "numero_contrato": numero_contrato,
        "modalidad": modalidad,
        "municipio": municipio,
        "departamento": departamento,
        "entidad": entidad,
        "nombre_proyecto": nombre_proyecto,
        "bpin": bpin,
        "valor_total": valor_total,
        "sector": sector,
        "codigo_ciiu": codigo_ciiu,
        "codigos_unspsc": codigos_unspsc,
        "duracion": str(duracion),
        "objeto": objeto,
        "plan_desarrollo": plan_desarrollo,
        "fuente_financiacion": fuente,
        "responsable": responsable,
        "cargo": cargo,
        "ano": str(datetime.now().year),
        "letterhead_file": letterhead_file
    }


def render_dts_form():
    """Render input form for DTS (Documento Técnico de Soporte)"""
    
    # Data extraction option
    extracted = render_data_upload_option("dts", "dts")
    
    st.markdown('<p class="section-header">Datos del Proyecto</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        municipio = st.text_input("Municipio *", placeholder="Ej: San Pablo", key="dts_municipio")
        departamento = st.text_input("Departamento *", placeholder="Ej: Bolívar", key="dts_depto")
        entidad = st.text_input("Entidad *", placeholder="Ej: Alcaldía Municipal", key="dts_entidad")
        bpin = st.text_input("Código BPIN", placeholder="Ej: 2024000001367", key="dts_bpin")
    
    with col2:
        nombre_proyecto = st.text_input("Nombre del Proyecto *", placeholder="Ej: Subsidio de Servicios Públicos", key="dts_proyecto")
        valor_total = st.text_input("Valor Total (COP) *", placeholder="Ej: 1200532612", key="dts_valor")
        duracion = st.number_input("Duración (días)", min_value=1, value=365, key="dts_duracion")
    
    st.markdown('<p class="section-header">Planes de Desarrollo</p>', unsafe_allow_html=True)
    
    programa = st.text_input(
        "Programa",
        placeholder="Ej: 4002 - Usuarios beneficiados con subsidios al consumo del servicio",
        key="dts_programa"
    )
    
    subprograma = st.text_input(
        "Subprograma",
        placeholder="Ej: Agua de vida con Identidad Bolivarense",
        key="dts_subprograma"
    )
    
    st.markdown('<p class="section-header">Objeto y Descripción</p>', unsafe_allow_html=True)
    
    objeto = st.text_area(
        "Objeto del Proyecto *",
        placeholder="Describa el objeto del proyecto de subsidio...",
        height=80,
        key="dts_objeto"
    )
    
    descripcion_problema = st.text_area(
        "Descripción del Problema",
        placeholder="Describa la situación actual y el problema a resolver...",
        height=100,
        key="dts_problema"
    )
    
    st.markdown('<p class="section-header">Membrete/Letterhead</p>', unsafe_allow_html=True)
    
    letterhead_file = st.file_uploader(
        "Subir plantilla con membrete (.docx)",
        type=["docx"],
        help="Suba un archivo .docx con el encabezado y pie de página de la alcaldía.",
        key="dts_letterhead"
    )
    
    st.markdown('<p class="section-header">Responsable</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        responsable = st.text_input("Nombre del Responsable *", placeholder="Ej: Carlos Augusto Gil Delgado", key="dts_responsable")
    with col2:
        cargo = st.text_input("Cargo", value="Secretario de Planeación Municipal", key="dts_cargo")
    
    return {
        "municipio": municipio,
        "departamento": departamento,
        "entidad": entidad,
        "bpin": bpin,
        "nombre_proyecto": nombre_proyecto,
        "valor_total": valor_total,
        "duracion": str(duracion),
        "programa": programa,
        "subprograma": subprograma,
        "objeto": objeto,
        "descripcion_problema": descripcion_problema,
        "responsable": responsable,
        "cargo": cargo,
        "letterhead_file": letterhead_file
    }


def render_certificaciones_form():
    """Render input form for Presentación y Certificaciones"""
    
    # Data extraction option
    extracted = render_data_upload_option("certificaciones", "cert")
    
    st.markdown('<p class="section-header">Datos del Proyecto</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        municipio = st.text_input("Municipio *", placeholder="Ej: San Pablo", key="cert_municipio")
        departamento = st.text_input("Departamento *", placeholder="Ej: Bolívar", key="cert_depto")
        entidad = st.text_input("Entidad *", placeholder="Ej: Alcaldía Municipal", key="cert_entidad")
        bpin = st.text_input("Código BPIN", placeholder="Ej: 2024000001367", key="cert_bpin")
    
    with col2:
        nombre_proyecto = st.text_input("Nombre del Proyecto *", placeholder="Ej: Subsidio de Servicios Públicos", key="cert_proyecto")
        valor_total = st.text_input("Valor Total (COP) *", placeholder="Ej: 1662485076", key="cert_valor")
        alcalde = st.text_input("Nombre del Alcalde *", placeholder="Ej: Jair Acevedo Cavadía", key="cert_alcalde")
    
    st.markdown('<p class="section-header">Plan de Desarrollo</p>', unsafe_allow_html=True)
    
    plan_desarrollo = st.text_input(
        "Plan de Desarrollo Municipal",
        placeholder="Ej: San Pablo Mejor 2024-2027",
        key="cert_plan"
    )
    
    st.markdown('<p class="section-header">Membrete/Letterhead</p>', unsafe_allow_html=True)
    
    letterhead_file = st.file_uploader(
        "Subir plantilla con membrete (.docx)",
        type=["docx"],
        help="Suba un archivo .docx con el encabezado y pie de página de la alcaldía.",
        key="cert_letterhead"
    )
    
    st.markdown('<p class="section-header">Responsable (Secretario de Planeación)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        responsable = st.text_input("Nombre del Responsable *", placeholder="Ej: Carlos Augusto Gil Delgado", key="cert_responsable")
    with col2:
        cargo = st.text_input("Cargo", value="Secretario de Planeación Municipal", key="cert_cargo")
    
    return {
        "municipio": municipio,
        "departamento": departamento,
        "entidad": entidad,
        "bpin": bpin,
        "nombre_proyecto": nombre_proyecto,
        "valor_total": valor_total,
        "alcalde": alcalde,
        "plan_desarrollo": plan_desarrollo,
        "responsable": responsable,
        "cargo": cargo,
        "letterhead_file": letterhead_file
    }


def render_mga_subsidios_form():
    """Render input form for MGA Subsidios document"""
    
    # Data extraction option
    extracted = render_data_upload_option("mga_subsidios", "mga")
    
    st.markdown('<p class="section-header">Datos Básicos del Proyecto</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        municipio = st.text_input("Municipio *", value=extracted.get("municipio", ""), placeholder="Ej: San Pablo", key="mga_municipio")
        departamento = st.text_input("Departamento *", value=extracted.get("departamento", ""), placeholder="Ej: Bolívar", key="mga_depto")
        entidad = st.text_input("Entidad *", value=extracted.get("entidad", ""), placeholder="Ej: Alcaldía Municipal", key="mga_entidad")
        bpin = st.text_input("Código BPIN", value=extracted.get("bpin", ""), placeholder="Ej: 2024000001367", key="mga_bpin")
        identificador = st.text_input("Identificador", placeholder="Ej: 1649979", key="mga_identificador")
    
    with col2:
        nombre_proyecto = st.text_input("Nombre del Proyecto *", value=extracted.get("nombre_proyecto", ""), placeholder="Ej: Subsidio de Servicios Públicos", key="mga_proyecto")
        valor_total = st.text_input("Valor Total (COP) *", value=extracted.get("valor_total", ""), placeholder="Ej: 1662485076", key="mga_valor")
        duracion = st.number_input("Duración (días)", min_value=1, value=365, key="mga_duracion")
        fecha_creacion = st.text_input("Fecha Creación", value=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), key="mga_fecha")
    
    st.markdown('<p class="section-header">Planes de Desarrollo</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        plan_nacional = st.text_input(
            "Plan Nacional de Desarrollo",
            value=extracted.get("plan_nacional", "(2022-2026) Colombia Potencia Mundial de la Vida"),
            key="mga_plan_nacional"
        )
        plan_departamental = st.text_input(
            "Plan Departamental",
            value=extracted.get("plan_departamental", ""),
            placeholder="Ej: Bolívar Me Enamora 2024-2027",
            key="mga_plan_depto"
        )
    with col2:
        plan_municipal = st.text_input(
            "Plan Municipal",
            value=extracted.get("plan_municipal", ""),
            placeholder="Ej: San Pablo Mejor 2024-2027",
            key="mga_plan_mun"
        )
    
    st.markdown('<p class="section-header">Membrete/Letterhead</p>', unsafe_allow_html=True)
    
    letterhead_file = st.file_uploader(
        "Subir plantilla con membrete (.docx)",
        type=["docx"],
        help="Suba un archivo .docx con el encabezado y pie de página.",
        key="mga_letterhead"
    )
    
    st.markdown('<p class="section-header">Responsable</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        responsable = st.text_input("Nombre del Responsable *", value=extracted.get("responsable", ""), placeholder="Ej: Carlos Augusto Gil Delgado", key="mga_responsable")
    with col2:
        cargo = st.text_input("Cargo", value=extracted.get("cargo", "Secretario de Planeación Municipal"), key="mga_cargo")
    
    return {
        "municipio": municipio,
        "departamento": departamento,
        "entidad": entidad,
        "bpin": bpin,
        "identificador": identificador,
        "nombre_proyecto": nombre_proyecto,
        "valor_total": valor_total,
        "duracion": str(duracion),
        "fecha_creacion": fecha_creacion,
        "plan_nacional": plan_nacional,
        "plan_departamental": plan_departamental,
        "plan_municipal": plan_municipal,
        "responsable": responsable,
        "cargo": cargo,
        "letterhead_file": letterhead_file
    }


def render_unified_form():
    """Render unified input form for generating ALL documents at once"""
    
    # Data extraction option
    extracted = render_data_upload_option("mga_subsidios", "unified")
    
    # 1. INFORMACIÓN GENERAL
    st.markdown('<p class="section-header">1. Información General del Proyecto (Todos)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        municipio = st.text_input("Municipio *", value=extracted.get("municipio", ""), placeholder="Ej: San Pablo", key="uni_municipio")
        departamento = st.text_input("Departamento *", value=extracted.get("departamento", ""), placeholder="Ej: Bolívar", key="uni_depto")
        entidad = st.text_input("Entidad *", value=extracted.get("entidad", ""), placeholder="Ej: Alcaldía Municipal", key="uni_entidad")
        bpin = st.text_input("Código BPIN", value=extracted.get("bpin", ""), placeholder="Ej: 2024000001367", key="uni_bpin")
    
    with col2:
        nombre_proyecto = st.text_input("Nombre del Proyecto *", value=extracted.get("nombre_proyecto", ""), placeholder="Ej: Construcción de...", key="uni_proyecto")
        valor_total = st.text_input("Valor Total (COP) *", value=extracted.get("valor_total", ""), placeholder="Ej: 100000000", key="uni_valor")
        duracion = st.number_input("Duración (días)", min_value=1, value=int(extracted.get("duracion", "90")) if str(extracted.get("duracion", "90")).isdigit() else 90, key="uni_duracion")
        fecha_creacion = datetime.now().strftime("%d/%m/%Y") # Auto-generated

    # 2. RESPONSABLES
    st.markdown('<p class="section-header">2. Responsables y Autoridades</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        responsable = st.text_input("Responsable del Proyecto *", value=extracted.get("responsable", ""), placeholder="Ej: Juan Pérez", key="uni_responsable")
        cargo = st.text_input("Cargo del Responsable", value=extracted.get("cargo", "Secretario de Planeación"), key="uni_cargo")
    with col2:
        alcalde = st.text_input("Nombre del Alcalde (Certificaciones)", value=extracted.get("alcalde", ""), placeholder="Ej: María Rodríguez", key="uni_alcalde")

    # 3. CONTRATACIÓN Y JURÍDICA
    st.markdown('<p class="section-header">3. Detalles de Contratación (Estudios Previos / Sector)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        obj_contractual = st.text_area("Objeto Contractual", value=extracted.get("objeto", ""), height=100, key="uni_objeto")
        modalidad = st.selectbox("Modalidad de Selección", ["Contratación Directa", "Licitación Pública", "Selección Abreviada", "Concurso de Méritos", "Mínima Cuantía", "Convenio Interadministrativo"], key="uni_modalidad")
        numero_contrato = st.text_input("Número de Contrato (Análisis Sector)", placeholder="Ej: 001-2025 (Si aplica)", key="uni_num_contrato")
    with col2:
        necesidad = st.text_area("Necesidad / Justificación / Descripción Problema", value=extracted.get("descripcion", ""), height=100, key="uni_necesidad", help="Se usará para Estudios Previos y DTS")
        alcance = st.text_area("Alcance (Actividades Principales)", value=extracted.get("alcance", ""), height=100, key="uni_alcance", help="Lista de actividades principales para Estudio Previos")
        fuente = st.text_input("Fuente de Financiación", value="Recursos Propios", key="uni_fuente")
        cdp_codigo = st.text_input("Código CDP (Opcional)", placeholder="Ej: 20260108-3", key="uni_cdp")
        
    st.markdown('<p class="section-header">3.1 Presupuesto (Detalle)</p>', unsafe_allow_html=True)
    rubros = st.text_area("Rubros / Desglose Presupuestal", value="Honorarios: 60%\nGastos Operativos: 40%", height=80, key="uni_rubros", help="Desglose para Estudios Previos")

    # 4. TÉCNICO Y SECTORIAL
    st.markdown('<p class="section-header">4. Información Técnica y Sectorial</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        sector = st.text_input("Sector Económico", value=extracted.get("sector", ""), placeholder="Ej: Transporte / Saneamiento", key="uni_sector")
        programa = st.text_input("Programa (DTS)", placeholder="Ej: 4002 - Usuarios beneficiados...", key="uni_programa")
    with col2:
        unspsc = st.text_input("Códigos UNSPSC", placeholder="Ej: 43210000, 72101500", key="uni_unspsc")
        codigo_ciiu = st.text_input("Código CIIU", placeholder="Ej: 7110", key="uni_ciiu")
        subprograma = st.text_input("Subprograma (DTS)", placeholder="Ej: Agua de vida...", key="uni_subprograma")
        
    # 5. CONTEXTO / DUMP
    st.markdown('<p class="section-header">5. Contexto del Documento (Dump Data)</p>', unsafe_allow_html=True)
    st.info("ℹ️ Texto extraído del archivo. Se usará como contexto adicional para generar secciones faltantes.")
    
    context_dump = st.text_area(
        "Texto Extraído / Contexto Adicional",
        value=extracted.get("context_dump", ""),
        height=200,
        placeholder="Aquí aparecerá el texto completo extraído del archivo de datos...",
        key="uni_context_dump"
    )

    st.markdown('<p class="section-header">6. Planes de Desarrollo (MGA / Certificaciones)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        plan_nacional = st.text_input("Plan Nacional", value=extracted.get("plan_nacional", "(2022-2026) Colombia Potencia Mundial de la Vida"), key="uni_pnd")
        plan_municipal = st.text_input("Plan Municipal", value=extracted.get("plan_municipal", ""), placeholder="Ej: San Pablo Mejor 2024-2027", key="uni_pm")
    with col2:
        plan_departamental = st.text_input("Plan Departamental", value=extracted.get("plan_departamental", ""), placeholder="Ej: Bolívar Me Enamora", key="uni_pd")

    st.markdown('<p class="section-header">Opcional: Membrete</p>', unsafe_allow_html=True)
    letterhead_file = st.file_uploader("Subir plantilla (.docx)", type=["docx"], key="uni_letterhead")

    # Construct unified data object
    timestamp = datetime.now().strftime("%d/%m/%Y")
    
    return {
        # Common
        "municipio": municipio,
        "departamento": departamento,
        "entidad": entidad,
        "bpin": bpin,
        "nombre_proyecto": nombre_proyecto,
        "valor_total": valor_total,
        "duracion": str(duracion),
        "fecha": timestamp,
        "fecha_creacion": timestamp,
        "responsable": responsable,
        "cargo": cargo,
        "alcalde": alcalde, # Certificaciones specific
        
        # Estudios Previos
        "objeto": obj_contractual,
        "necesidad": necesidad,
        "alcance": alcance, # Added in previous step
        "rubros": rubros, # Added in previous step
        "modalidad": modalidad,
        "plazo": str(duracion),
        "fuente_financiacion": fuente,
        "cdp_data": {"cdp": cdp_codigo, "fecha": timestamp, "valor": valor_total}, # Synthesize CDP data
        "tipo_proyecto": modalidad,
        "lugar": f"{municipio}, {departamento}",
        
        # Analisis Sector
        "sector": sector,
        "codigos_unspsc": unspsc,
        "codigo_ciiu": codigo_ciiu,
        "numero_contrato": numero_contrato if numero_contrato else "POR DEFINIR",
        "plan_desarrollo": plan_municipal, # Map to specific field
        
        # DTS
        "descripcion_problema": necesidad, # Reuse
        "programa": programa,
        "subprograma": subprograma, # Added in previous step
        "poblacion_beneficiada": "Población general del municipio",
        
        # MGA
        "plan_nacional": plan_nacional,
        "plan_departamental": plan_departamental,
        "plan_municipal": plan_municipal,
        "identificador": bpin,
        
        # Files
        "letterhead_file": letterhead_file,
        "context_dump": context_dump, # Raw text for fallback
    }


def generate_document(doc_type: str, data: dict, model: str):
    """Generate document using selected model"""
    try:
        # Get LLM based on selection
        llm = get_llm(model)
        
        # Get section toggles from session state
        section_toggles = st.session_state.get('section_toggles', {})
        data['section_toggles'] = section_toggles
        
        # Get generation mode and edit instructions
        generation_mode = st.session_state.get('generation_mode', 'crear_nuevo')
        data['generation_mode'] = generation_mode
        
        # Get edit instructions if in update mode
        if generation_mode == 'actualizar_existente':
            edit_instructions = st.session_state.get('edit_instructions', '')
            data['edit_instructions'] = edit_instructions
        
        # Create generator based on document type
        if doc_type == "estudios_previos":
            generator = EstudiosPreviosGenerator(llm)
            result = generator.generate_complete(data)
            return result.get("documento_completo", ""), result.get("filepath")
        elif doc_type == "analisis_sector":
            generator = AnalisisSectorGenerator(llm)
            result = generator.generate_complete(data)
            return result.get("documento_completo", ""), result.get("filepath")
        elif doc_type == "dts":
            generator = DTSGenerator(llm)
            result = generator.generate_complete(data)
            return result.get("documento_completo", ""), result.get("filepath")
        elif doc_type == "certificaciones":
            generator = CertificacionesGenerator(llm)
            result = generator.generate_complete(data)
            return result.get("documento_completo", ""), result.get("filepath")
        else:  # mga_subsidios
            generator = MGASubsidiosGenerator(llm)
            result = generator.generate_complete(data)
            return result.get("documento_completo", ""), result.get("filepath")
        
    except Exception as e:
        st.error(f"Error al generar documento: {str(e)}")
        return None, None


def main():
    """Main application"""
    # Render sidebar and get selected model
    selected_model = render_sidebar()
    
    # Main header
    st.markdown(f'<p class="main-header">{APP_TITLE}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header">{APP_DESCRIPTION}</p>', unsafe_allow_html=True)
    
    # Document type selection
    st.markdown("**Seleccionar Tipo de Documento**")
    
    doc_type = st.radio(
        "Tipo de documento a generar:",
        options=["unified", "estudios_previos", "analisis_sector", "dts", "certificaciones", "mga_subsidios"],
        format_func=lambda x: {
            "unified": "🚀 Generar Todo (Unified Mode)",
            "estudios_previos": "Estudios Previos", 
            "analisis_sector": "Análisis del Sector", 
            "dts": "DTS (Documento Técnico)",
            "certificaciones": "Certificaciones",
            "mga_subsidios": "MGA Subsidios"
        }.get(x, x),
        horizontal=True,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Render appropriate form
    if doc_type == "unified":
        data = render_unified_form()
    elif doc_type == "estudios_previos":
        data = render_estudios_previos_form()
    elif doc_type == "analisis_sector":
        data = render_analisis_sector_form()
    elif doc_type == "dts":
        data = render_dts_form()
    elif doc_type == "certificaciones":
        data = render_certificaciones_form()
    else:  # mga_subsidios
        data = render_mga_subsidios_form()
    
    st.markdown("---")
    
    # Generate button
    if st.button("Generar Documento(s)", type="primary"):
        # Validate data
        project_name = data.get("nombre_proyecto", data.get("proyecto", ""))
        
        if not project_name:
            st.warning("⚠️ Por favor ingrese al menos el nombre del proyecto.")
            return

        # Clear previous generation state
        st.session_state.generated_content = None
        st.session_state.generated_file = None

        # Show spinner and generate
        with st.spinner("Generando documento(s) con Inteligencia Artificial..."):
            
            if doc_type == "unified":
                generator = UnifiedGenerator()
                
                # Progress bar for unified generation
                progress_bar = st.progress(0, text="Iniciando generación paralela de 5 documentos...")
                
                # Execute generation
                result = generator.generate_all(data, selected_model)
                
                progress_bar.progress(100, text="Generación Completada!")
                
                if result["success"]:
                    st.success(f"✅ Se generaron exitosamente {len(result['results'])} documentos.")
                    
                    # Show individual results
                    for res in result["results"]:
                        if res["status"] == "success":
                            file_name = os.path.basename(res["file"])
                            st.write(f"📄 {res['type'].replace('_', ' ').title()}: **{file_name}**")
                        else:
                            st.error(f"❌ Error en {res['type']}: {res.get('error', 'Unknown')}")
                    
                    # Unified ZIP Download
                    if result.get("zip_file"):
                        with open(result["zip_file"], "rb") as f:
                            st.download_button(
                                label="⬇️ Descargar TODOS los Documentos (ZIP)",
                                data=f,
                                file_name=os.path.basename(result["zip_file"]),
                                mime="application/zip",
                                key="unified_download"
                            )
                else:
                    st.error("❌ Ocurrió un error al generar los documentos.")
                    
            else:
                # Individual generation
                content, filepath = generate_document(doc_type, data, selected_model)
                
                if content and filepath:
                    # Save generation to session state for persistence
                    st.session_state.generated_content = content
                    st.session_state.generated_file = filepath
                    
                    st.success("✅ Documento generado exitosamente!")
                    
                    # Download button
                    with open(filepath, "rb") as f:
                        file_name = os.path.basename(filepath)
                        st.download_button(
                            label="⬇️ Descargar Documento (Word/PDF)",
                            data=f,
                            file_name=file_name,
                            mime="application/pdf" if filepath.endswith(".pdf") else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        )
                    
                    # Preview expander
                    with st.expander("Ver contenido generado", expanded=False):
                        st.markdown(content)
        
    # Reset button
    if st.button("Generar Nuevo Documento"):
        st.session_state.generated_content = None
        st.session_state.generated_file = None
        st.rerun()


if __name__ == "__main__":
    main()
