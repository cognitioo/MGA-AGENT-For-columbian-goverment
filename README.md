# 🇨🇴 MGA AI Agent

**Generador Inteligente de Documentos para la Metodología General Ajustada (MGA)**

Herramienta de IA especializada en generar documentos de contratación pública colombiana, diseñada para asesores de alcaldías municipales y empresas de servicios públicos.

---

## 📑 Tabla de Contenidos

- [Características](#-características)
- [Casos de Uso](#-casos-de-uso)
- [Funcionalidades Actuales](#-funcionalidades-actuales)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Guía de Uso Detallada](#-guía-de-uso-detallada)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Personalización](#-personalización)
- [Solución de Problemas](#-solución-de-problemas)

---

## ✨ Características

| Característica | Descripción |
|----------------|-------------|
| **Multi-modelo IA** | Soporte para Groq Llama, Google Gemini, OpenAI GPT-4, Anthropic Claude |
| **Documentos MGA** | Genera Estudios Previos y Análisis del Sector conformes a la normatividad colombiana |
| **Membrete Configurable** | Subir plantilla .docx con encabezado/pie de página de cualquier alcaldía |
| **Dos Modos de Trabajo** | Crear documento desde cero o actualizar uno existente |
| **Secciones Personalizables** | Activar/desactivar secciones según necesidad |
| **Plantillas Predefinidas** | Estándar, Simplificado, Completo |
| **Gráficos Automáticos** | Incluye gráfico PIB y tabla SMLMV histórica |
| **Interfaz en Español** | Diseñada para usuarios colombianos |

---

## 🎯 Casos de Uso

### Caso 1: Crear MGA desde Cero con Datos POAI
>
> **Escenario**: El municipio tiene un nuevo proyecto y necesita generar todos los documentos de soporte desde cero.

1. Abrir la aplicación
2. Seleccionar "Crear desde cero"
3. Ingresar los datos del POAI (Plan Operativo Anual de Inversiones)
4. Generar Estudios Previos y Análisis del Sector
5. Descargar documentos Word listos para firmar

### Caso 2: Actualizar MGA del Año Anterior
>
> **Escenario**: Se tiene un MGA del año anterior y solo se necesitan actualizar valores, fechas y algunos datos.

1. Seleccionar "Actualizar existente"
2. Subir el documento anterior (PDF o DOCX)
3. Describir los cambios: "Actualizar valores POAI 2025, cambiar fechas a enero 2026"
4. Modificar solo los campos que cambiaron
5. Generar documento actualizado

### Caso 3: Generar Documento Simplificado
>
> **Escenario**: Se necesita un documento rápido con solo las secciones esenciales.

1. Seleccionar plantilla "Simplificado" en el sidebar
2. Solo se incluirán: OBJETO, ALCANCE, NECESIDAD, RIESGOS, ESTIMACIÓN
3. Generar documento más corto y directo

### Caso 4: Trabajar con Diferente Municipio
>
> **Escenario**: El asesor trabaja con varias alcaldías y cada una tiene su membrete diferente.

1. Preparar archivo .docx con el membrete de la alcaldía
2. Subir el membrete en el campo "Membrete/Letterhead"
3. El documento generado usará automáticamente ese encabezado/pie de página

---

## 🔧 Funcionalidades Actuales

### Documentos Generados

#### 1. Estudios Previos

Documento que justifica la contratación y contiene:

- **OBJETO**: Descripción del contrato/convenio
- **ALCANCE**: Actividades y entregables
- **Descripción de la Necesidad**: Problema a resolver
- **Análisis Técnico**: Especificaciones del proyecto
- **Obligaciones del Municipio**: Sección 4
- **Obligaciones del Contratista**: Sección 5
- **Presupuesto**: Desglose de rubros
- **CDP (Certificado de Disponibilidad Presupuestal)**: Tabla en sección 7
- **Firma del Responsable**: Con cargo

#### 2. Análisis del Sector

Documento de análisis de mercado que incluye:

- **OBJETO, ALCANCE, NECESIDAD, INTRODUCCIÓN, DEFINICIONES**
- **1. DESARROLLO DEL ESTUDIO DEL SECTOR**
  - 1.1 Banco de Programas y Proyectos (BPIN)
  - 1.2 Consideraciones para la realización
  - 1.3 Preparación del Estudio
  - 1.4 Estructura (mercado, oferta, demanda)
- **1.5 ANÁLISIS DEL SECTOR**
  - Descripción sector económico
  - Sector terciario
  - Comportamiento economía nacional + Gráfico PIB
  - Variables económicas + Tabla SMLMV (2000-2025)
  - Relevancia para el proyecto
  - Perspectivas legales
  - Riesgos con matriz de mitigación
- **2. ESTUDIOS DEL SECTOR EN CONTRATACIÓN**
- **3. CRITERIOS MIPYME Y EMPRESAS DE MUJERES**
- **4. RECOMENDACIONES ANÁLISIS ESTADÍSTICO**
- **5. FUENTES DE INFORMACIÓN**
- **6. HERRAMIENTAS DE BÚSQUEDA**
- **7. ESTIMACIÓN Y JUSTIFICACIÓN DEL VALOR**
- **Firma del Responsable**

### Controles del Sidebar

| Control | Función |
|---------|---------|
| **Modo de Generación** | Crear nuevo vs Actualizar existente |
| **Documento Base** | Subir MGA anterior para actualizar |
| **Instrucciones de Edición** | Describir qué cambios hacer |
| **Modelo de IA** | Seleccionar proveedor LLM |
| **Plantilla** | Estándar, Simplificado, Completo, Personalizado |
| **Secciones Activas** | Checkboxes para activar/desactivar cada sección |

### Secciones Controlables

```
☑ OBJETO           ☑ Gráfico PIB
☑ ALCANCE          ☑ Tabla SMLMV
☑ Necesidad        ☑ Riesgos
☑ Introducción     ☑ 2. Contratación
☑ Definiciones     ☑ Recomendaciones
☑ 1. Desarrollo    ☑ Fuentes
☑ 1.5 Análisis     ☑ Estimación $
```

---

## 📋 Requisitos

### Sistema

- **Python**: 3.9 o superior
- **Sistema Operativo**: Windows 10/11, macOS, Linux
- **RAM**: Mínimo 4GB (8GB recomendado)
- **Conexión a Internet**: Requerida para API de IA

### API Keys (al menos una)

| Proveedor | Costo Aproximado | Velocidad | Calidad Español |
|-----------|------------------|-----------|-----------------|
| **Groq** | Bajo (~$5/mes) | Muy rápido | Buena |
| **Gemini** | Bajo (~$5/mes) | Rápido | Buena |
| **OpenAI** | Medio (~$20/mes) | Medio | Excelente |
| **Anthropic** | Medio (~$15/mes) | Medio | Muy buena |

---

## 🚀 Instalación

### Paso 1: Preparar Python

```bash
# Verificar versión de Python
python --version  # Debe ser 3.9 o superior

# Si no tiene Python, descargar de: https://www.python.org/downloads/
```

### Paso 2: Obtener el Proyecto

```bash
# El proyecto está en:
cd C:\Users\user\Desktop\AI_Agent
```

### Paso 3: Crear Entorno Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Paso 4: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 5: Verificar Instalación

```bash
pip list | findstr streamlit
# Debe mostrar: streamlit 1.xx.x
```

---

## ⚙️ Configuración

### Configurar API Keys

1. Copiar el archivo de ejemplo:

```bash
copy .env.example .env
```

1. Editar `.env` y agregar su API key:

```env
# Elegir UNO de los siguientes:

# Opción 1: Groq (Recomendado - económico y rápido)
GROQ_API_KEY=gsk_su_clave_aqui

# Opción 2: Google Gemini
GOOGLE_API_KEY=AIza_su_clave_aqui

# Opción 3: OpenAI
OPENAI_API_KEY=sk-su_clave_aqui

# Opción 4: Anthropic
ANTHROPIC_API_KEY=sk-ant-su_clave_aqui
```

### Obtener API Keys

| Proveedor | URL para obtener clave |
|-----------|------------------------|
| Groq | <https://console.groq.com/keys> |
| Gemini | <https://makersuite.google.com/app/apikey> |
| OpenAI | <https://platform.openai.com/api-keys> |
| Anthropic | <https://console.anthropic.com/> |

---

## 📖 Guía de Uso Detallada

### Iniciar la Aplicación

```bash
# Asegurarse de estar en el directorio correcto
cd C:\Users\user\Desktop\AI_Agent

# Activar entorno virtual (si lo creó)
venv\Scripts\activate

# Ejecutar aplicación
streamlit run app.py
```

El navegador abrirá automáticamente: **<http://localhost:8501>**

### Pantalla Principal

```
┌─────────────────────────────────────────────────────────┐
│  🛠️ MGA Agent (Sidebar)    │  📋 MGA AI Agent          │
│  ─────────────────────────  │  Generador de Documentos  │
│                             │                           │
│  📋 Modo de Generación      │  ○ Estudios Previos      │
│  ○ Crear desde cero         │  ● Análisis del Sector   │
│  ○ Actualizar existente     │                           │
│                             │  ─────────────────────────│
│  🤖 Modelo de IA            │  Datos del Contrato       │
│  [Groq - Llama ▼]           │  [Formulario...]          │
│                             │                           │
│  📑 Plantilla               │  [Generar Documento]      │
│  [Estándar ▼]               │                           │
│                             │                           │
│  ▸ 📊 Secciones Activas     │                           │
└─────────────────────────────────────────────────────────┘
```

### Flujo de Trabajo: Estudios Previos

1. **Seleccionar documento**: "Estudios Previos"

2. **Completar Datos del Proyecto**:
   - Municipio: `San Pablo`
   - Departamento: `Bolívar`
   - Entidad Contratante: `Alcaldía Municipal de San Pablo`
   - Código BPIN: `2024000001367`
   - Tipo de Proyecto: `Convenio Interadministrativo`
   - Valor Total: `85000000`
   - Plazo: `120` días
   - Fuente: `Recursos Propios`

3. **Completar Descripción**:
   - Necesidad: (Describir el problema)
   - Objeto: (Describir el contrato)
   - Alcance: (Listar actividades)
   - Rubros: (Desglose presupuestal)

4. **Completar Obligaciones** (Secciones 4 y 5):
   - Obligaciones del Municipio
   - Obligaciones del Contratista

5. **Completar CDP** (Sección 7):
   - Código CDP: `20260108-3`
   - Fecha: `08/01/2026`
   - Rubro: `2.3.2.02.02.009.45.25`
   - Fuente: `SGP – Propósito General`
   - Valor: `$17.400.000,00`

6. **Subir Membrete** (opcional):
   - Cargar archivo .docx con encabezado de la alcaldía

7. **Responsable**:
   - Nombre: `Carlos Augusto Gil Delgado`
   - Cargo: `Secretario de Planeación Municipal`

8. **Clic en "Generar Documento"**

9. **Revisar y Descargar**: Vista previa + botón de descarga Word

### Flujo de Trabajo: Análisis del Sector

Similar al anterior, pero con campos adicionales:

- Número de Contrato
- Modalidad (Convenio, Licitación, etc.)
- Sector
- Código CIIU
- Códigos UNSPSC
- Plan de Desarrollo Relacionado

---

## 📁 Estructura del Proyecto

```
AI_Agent/
│
├── 📄 app.py                      # Aplicación principal Streamlit
├── 📄 config.py                   # Configuración modelos LLM
├── 📄 requirements.txt            # Dependencias Python
├── 📄 README.md                   # Esta documentación
├── 📄 .env                        # API Keys (no compartir)
├── 📄 .env.example                # Ejemplo de configuración
│
├── 📁 generators/                 # Generadores de documentos
│   ├── estudios_previos_builder.py    # Constructor Word Estudios
│   ├── estudios_previos_generator.py  # Lógica IA Estudios
│   ├── analisis_sector_builder.py     # Constructor Word Análisis
│   ├── analisis_sector_generator.py   # Lógica IA Análisis
│   └── docx_builder.py                # Utilidades Word
│
├── 📁 prompts/                    # Templates para IA
│   ├── base_prompts.py                # Contexto MGA base
│   ├── estudios_previos.py            # Prompts Estudios
│   └── analisis_sector_structured.py  # Prompts Análisis
│
├── 📁 templates/                  # Plantillas membrete
│   └── plantilla_membrete.docx
│
└── 📁 output/                     # Documentos generados
    ├── Estudios_Previos_*.docx
    └── Analisis_Sector_*.docx
```

---

## 🎨 Personalización

### Cambiar Secciones Incluidas

1. En el sidebar, expandir **"📊 Secciones Activas"**
2. Marcar/desmarcar según necesidad:

```
Para documento rápido (Simplificado):
☑ OBJETO ☑ ALCANCE ☑ Necesidad ☑ Riesgos ☑ Estimación

Para documento completo:
☑ Todas las secciones marcadas
```

### Usar Diferentes Membretes

Crear archivo Word con:

1. Encabezado con logo de la alcaldía
2. Pie de página con información institucional
3. Guardar como .docx
4. Subir al generar documento

### Cambiar Modelo de IA

En el sidebar:

- **Groq**: Más rápido, económico
- **Gemini**: Balance calidad/costo
- **OpenAI**: Mejor español
- **Anthropic**: Alta calidad general

---

## 🔧 Solución de Problemas

| Problema | Causa | Solución |
|----------|-------|----------|
| "Error de API Key" | Key incorrecta o expirada | Verificar `.env`, regenerar key |
| "Error 413 tokens" | Prompt muy largo | Usar plantilla simplificada |
| "Gráficos no aparecen" | Matplotlib no instalado | `pip install matplotlib` |
| "Documento vacío" | Campos requeridos vacíos | Completar campos con * |
| "Sección sin contenido" | IA no generó esa parte | Re-generar o editar manualmente |
| "Membrete no aparece" | Archivo .docx inválido | Crear nuevo archivo Word limpio |
| "App no inicia" | Dependencias faltantes | `pip install -r requirements.txt` |

### Logs de Error

Si hay errores, revisar la terminal donde ejecutó `streamlit run app.py` para ver mensajes detallados.

---

## 📞 Soporte

Para reportar errores o solicitar nuevas funciones:

- Documentar el error con capturas de pantalla
- Incluir el mensaje de error de la terminal
- Describir los pasos para reproducir el problema

---

## 🔮 Roadmap (Futuras Mejoras)

- [ ] Reportes para plataforma SUI
- [ ] Estudios tarifarios basados en decretos
- [ ] Extracción automática de datos desde PDF
- [ ] Más tipos de documentos MGA

---

## 📄 Licencia

Proyecto privado - © 2026 - Todos los derechos reservados

---

**Desarrollado para la gestión de proyectos públicos en Colombia 🇨🇴**

*Basado en la Metodología General Ajustada (MGA) del Departamento Nacional de Planeación (DNP)*
