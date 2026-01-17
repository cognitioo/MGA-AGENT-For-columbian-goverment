"""
Estudios Previos (Prior Studies) Structured Prompt Templates
Returns structured JSON content for all 12 sections
"""

from .base_prompts import MGA_CONTEXT, LEGAL_REFERENCES

ESTUDIOS_PREVIOS_SYSTEM_STRUCTURED = f"""
{MGA_CONTEXT}

Tu tarea es generar contenido estructurado para un documento de ESTUDIOS PREVIOS según el formato MGA colombiano.

{LEGAL_REFERENCES}

═══════════════════════════════════════════════════════════════════════════════
                    ESTRUCTURA DEL DOCUMENTO ESTUDIOS PREVIOS
═══════════════════════════════════════════════════════════════════════════════

El documento tiene 12 SECCIONES obligatorias. Debes generar contenido para TODAS:

1. MARCO LEGAL - Referencias normativas que fundamentan la contratación
2. NECESIDAD QUE SATISFACE LA CONTRATACIÓN - Problema/necesidad a resolver
3. OBJETO Y ALCANCE - Qué se va a contratar y actividades
4. OBLIGACIONES DEL MUNICIPIO - Compromisos de la entidad contratante
5. OBLIGACIONES DEL CONTRATISTA - Compromisos del ejecutor
6. FUNDAMENTOS JURÍDICOS QUE SOPORTAN LA MODALIDAD DE SELECCIÓN
7. ANÁLISIS QUE SOPORTA EL VALOR ESTIMADO Y FORMA DE PAGO
8. ANÁLISIS DE RIESGOS - Riesgos identificados y mitigación
9. ANÁLISIS QUE SUSTENTA LA EXIGENCIA DE GARANTÍAS
10. PLAZO Y LUGAR DE EJECUCIÓN
11. SUPERVISIÓN - Quién supervisa y cómo
12. RESPONSABLES - Funcionario responsable del proceso

═══════════════════════════════════════════════════════════════════════════════
                    REGLAS DE GENERACIÓN
═══════════════════════════════════════════════════════════════════════════════

IMPORTANTE:
• Responde ÚNICAMENTE en formato JSON válido, sin explicaciones adicionales
• NO uses markdown. Usa texto plano con <br> para saltos de línea
• Para negritas, usa: **texto en negrita**
• Para viñetas, usa: • texto de viñeta
• NO incluyas títulos de sección en el contenido (se agregan automáticamente)
• GENERA contenido extenso y profesional para CADA sección
• USA el conocimiento normativo colombiano en tus respuestas
• NO dejes secciones vacías
"""

# Complete document structured prompt with all 12 sections
PROMPT_ESTUDIOS_PREVIOS_ESTRUCTURADO = """
Genera contenido estructurado para un documento de ESTUDIOS PREVIOS para contratación pública colombiana.

═══════════════════════════════════════════════════════════════════════════════
                    DATOS DEL PROYECTO (proporcionados por el usuario)
═══════════════════════════════════════════════════════════════════════════════

📍 UBICACIÓN:
- Municipio: {municipio}
- Departamento: {departamento}
- Lugar de ejecución: {lugar}

📂 CONTEXTO ADICIONAL DEL DOCUMENTO (DUMP DATA):
{context_dump}

🏛️ ENTIDAD:
- Entidad contratante: {entidad}
- Tipo de proyecto: {tipo_proyecto}
- Código BPIN (MGA): {bpin}

📋 DESCRIPCIÓN DEL PROYECTO:
NECESIDAD/PROBLEMA:
{necesidad}

OBJETO DEL CONVENIO/CONTRATO:
{objeto}

ALCANCE Y ACTIVIDADES:
{alcance}

💰 INFORMACIÓN FINANCIERA:
- Valor total: {valor_total} COP
- Fuente de financiación: {fuente_financiacion}
- Desglose presupuestal: {rubros}

⏱️ EJECUCIÓN:
- Plazo de ejecución: {plazo} días calendario
- Responsable del proceso: {responsable}
- Cargo: {cargo}

═══════════════════════════════════════════════════════════════════════════════
                    RESPUESTA REQUERIDA
═══════════════════════════════════════════════════════════════════════════════

RESPONDE ÚNICAMENTE CON UN JSON VÁLIDO. Genera contenido EXTENSO y PROFESIONAL para las 12 secciones:

{{
    "marco_legal": "Genera 4-5 párrafos extensos sobre el marco legal y normativo. Incluye:<br><br>La contratación del presente convenio interadministrativo se sustenta en el marco normativo que regula la planeación y la contratación pública en Colombia.<br><br>**Normatividad Constitucional**<br>• Artículo 209 de la Constitución Política – Principio de planeación y gestión pública.<br>• Artículos 365 a 370 – Servicios públicos inherentes a la finalidad social del Estado.<br><br>**Normatividad Legal**<br>• Ley 80 de 1993 – Estatuto General de Contratación de la Administración Pública, que establece los principios de igualdad, transparencia y selección objetiva. El Art. 25 determina la necesidad de justificar la contratación mediante estudios previos.<br>• Ley 1150 de 2007 – Medidas para la eficiencia y transparencia en la contratación, Art. 2 numeral 4 literal c) autoriza la contratación directa mediante convenios interadministrativos.<br>• Ley 1474 de 2011 – Estatuto Anticorrupción.<br>• Decreto 1082 de 2015 – Decreto Único Reglamentario del Sector Planeación Nacional, Art. 2.2.1.1.2.1.1 define los estudios y documentos previos.<br>• Ley 152 de 1994 – Ley Orgánica del Plan de Desarrollo, armonización con planes sectoriales.<br><br>Para proyectos de saneamiento, incluye normatividad ambiental específica como Resolución 0631 de 2015, Decreto 3930 de 2010, Resolución 1433 de 2004 y Resolución 1397 de 2018 sobre PSMV.",

    "necesidad": "Genera 4-5 párrafos extensos explicando la NECESIDAD que satisface la contratación. Describe:<br><br>El municipio de {municipio}, con una población estimada de XX habitantes, presenta [describir el problema específico basado en los datos proporcionados]. Esta situación genera [consecuencias negativas].<br><br>Desde el punto de vista técnico, [explicar aspectos técnicos del problema]. La ausencia de una solución adecuada implica [riesgos para la población].<br><br>La actualización/ejecución del proyecto es una necesidad urgente que permitirá:<br>• Cumplir con la normatividad vigente<br>• Mejorar la calidad de vida de los habitantes<br>• Proteger el medio ambiente<br>• Evitar sanciones de las autoridades competentes<br><br>Por tanto, la contratación propuesta responde a una necesidad real y urgente del municipio.",

    "objeto_alcance": "Genera 3-4 párrafos sobre el objeto y alcance, más una lista de actividades. El objeto del presente convenio interadministrativo es [usar el objeto proporcionado por el usuario].<br><br>El alcance del proyecto comprende las siguientes fases y actividades necesarias:<br><br>**Actividades principales:**<br>1. Planeación y coordinación institucional del proyecto.<br>2. [Actividad basada en el alcance proporcionado].<br>3. [Más actividades].<br>4. [Continuar con las actividades del alcance].<br>5. Socialización de resultados con la comunidad.<br>6. Gestión de validación ante las autoridades competentes.<br>7. Entrega de productos finales y cierre contractual.<br><br>El proyecto se desarrollará en un plazo de {plazo} días calendario.",

    "obligaciones": {{
        "municipio": "• Proveer la información cartográfica, hidrológica y de infraestructura requerida para el proyecto.<br>• Facilitar el acceso del equipo técnico a los sitios de ejecución.<br>• Garantizar la disponibilidad presupuestal y la ejecución del pago conforme al cronograma establecido.<br>• Designar al responsable del proyecto y al supervisor técnico.<br>• Difundir los resultados del plan a la comunidad y a los organismos de control.<br>• Aprobar los productos entregables en los plazos establecidos.<br>• Coordinar la convocatoria y logística de los procesos de socialización.<br>• Suscribir oportunamente las actas de inicio, seguimiento, ejecución, avances parciales y terminación.",
        "empresa": "• Ejecutar las actividades descritas en el alcance con la calidad y los plazos establecidos.<br>• Presentar informes técnicos parciales y un informe final del proyecto.<br>• Cumplir con las normas de seguridad, salud ocupacional y protección de datos.<br>• Gestionar la validación del proyecto ante las autoridades competentes y atender las observaciones que se generen.<br>• Mantener vigentes los seguros y pólizas de responsabilidad civil durante la ejecución.<br>• Conservar la documentación técnica y entregarla al municipio al término del contrato.<br>• Garantizar la calidad de los estudios, diseños y servicios definidos en el alcance."
    }},

    "fundamentos": "Genera 3-4 párrafos sobre los fundamentos jurídicos que soportan la modalidad de selección:<br><br>**Normatividad Constitucional**<br>• Artículo 2 de la Constitución Política – Define los fines esenciales del Estado: servir a la comunidad, promover la prosperidad general y garantizar los derechos y deberes consagrados.<br>• Artículo 209 – La función administrativa está al servicio del interés general bajo principios de igualdad, moralidad, eficacia, economía, celeridad, imparcialidad y publicidad.<br>• Artículo 268 – Reconoce la autonomía de departamentos y municipios para administrar recursos.<br><br>**Normatividad Legal**<br>• Ley 80 de 1993 – Art. 25 define la necesidad de estudios y documentos previos como soporte de los procesos contractuales.<br>• Ley 1150 de 2007 – Art. 2, numeral 4, literal c) establece la contratación directa en convenios interadministrativos cuando el objeto guarde relación directa con el objeto social de la entidad ejecutora.<br>• Decreto 1082 de 2015 – Art. 2.2.1.2.1.4.4 reglamenta los convenios interadministrativos.<br><br>**Jurisprudencia Aplicable**<br>• Sentencia C-671 de 1999 del Consejo de Estado – Reconoce la procedencia de convenios interadministrativos para cooperar en el cumplimiento de fines estatales.",

    "analisis_valor": "Genera contenido sobre el análisis que soporta el valor estimado y forma de pago:<br><br>El valor total estimado del convenio asciende a ${valor_total} COP (incluido IVA si aplica), determinado con base en los siguientes criterios:<br><br>**Criterios de estimación:**<br>• Análisis de precios del mercado para servicios similares.<br>• Histórico de contrataciones anteriores de la entidad.<br>• Presupuesto oficial registrado en el BPIN {bpin} de la plataforma MGA del DNP.<br>• Disponibilidad presupuestal del municipio de {municipio}.<br><br>**Forma de pago:**<br>El valor del convenio será cancelado bajo las siguientes condiciones:<br>• Anticipo (40%): Corresponde al cuarenta por ciento del valor total, desembolsado una vez suscrita el acta de inicio, contra presentación de garantía de anticipo.<br>• Pago final (60%): Corresponde al sesenta por ciento restante, previa presentación de certificación de recibo a satisfacción por parte del supervisor designado.<br><br>Los pagos se efectuarán en un plazo máximo de 30 días hábiles siguientes a la radicación de la factura y cumplimiento de requisitos.",

    "presupuesto": [
        {{"nombre": "Honorarios profesionales", "descripcion": "Consultoría técnica y jurídica.", "porcentaje": "55%", "valor": "Calcular según valor_total"}},
        {{"nombre": "Gastos operativos", "descripcion": "Desplazamientos, insumos, equipos.", "porcentaje": "30%", "valor": "Calcular según valor_total"}},
        {{"nombre": "Imprevistos", "descripcion": "Eventualidades y contingencias.", "porcentaje": "15%", "valor": "Calcular según valor_total"}}
    ],

    "riesgos": [
        {{"riesgo": "Demora en recolección de información", "descripcion": "Dificultades de acceso a la infraestructura.", "probabilidad": "Media", "mitigacion": "Coordinar permisos y cronograma con antelación."}},
        {{"riesgo": "Baja participación comunitaria", "descripcion": "Poca asistencia a talleres de socialización.", "probabilidad": "Media", "mitigacion": "Campaña de difusión por medios locales."}},
        {{"riesgo": "Observaciones de autoridades", "descripcion": "Ajustes técnicos requeridos.", "probabilidad": "Media", "mitigacion": "Revisión preliminar antes de radicación."}},
        {{"riesgo": "Cambios normativos", "descripcion": "Modificación de requisitos legales.", "probabilidad": "Baja", "mitigacion": "Monitoreo constante de normatividad."}}
    ],

    "garantias": "Genera contenido sobre las garantías exigidas conforme a la Ley 1150 de 2007 y Decreto 1082 de 2015:<br><br>En cumplimiento de lo establecido en el artículo 7 de la Ley 1150 de 2007 y el Decreto 1082 de 2015, el CONTRATISTA deberá constituir las siguientes garantías para amparar el cumplimiento de las obligaciones:<br><br>**a) Cumplimiento del contrato**<br>• Por el 10% del valor total del contrato.<br>• Vigencia: Igual al plazo de ejecución más cuatro (4) meses adicionales.<br>• Finalidad: Garantizar el cumplimiento de las obligaciones contractuales.<br><br>**b) Buen manejo del anticipo** (si aplica)<br>• Por el 100% del valor del anticipo.<br>• Vigencia: Hasta la liquidación del contrato.<br>• Finalidad: Garantizar la correcta inversión del anticipo otorgado.<br><br>**c) Salarios, prestaciones sociales e indemnizaciones del personal**<br>• Por el 5% del valor del contrato.<br>• Vigencia: Plazo de ejecución más tres (3) años.<br>• Finalidad: Proteger los derechos laborales.<br><br>**d) Responsabilidad civil extracontractual**<br>• Por una cuantía equivalente a 200 SMMLV.<br>• Vigencia: Por el plazo de ejecución del contrato.<br>• Finalidad: Cubrir daños a terceros.<br><br>Las garantías deberán presentarse dentro de los cinco (5) días hábiles siguientes a la firma del convenio y estarán sujetas a aprobación por parte de la entidad.",

    "plazo_lugar": "Genera contenido sobre el plazo y lugar de ejecución:<br><br>**Plazo de ejecución:**<br>El plazo de ejecución del presente convenio será de {plazo} días calendario, contados a partir de la suscripción del acta de inicio, previa aprobación de las garantías correspondientes.<br><br>**Lugar de ejecución:**<br>Las actividades del convenio se desarrollarán en la jurisdicción del municipio de {municipio}, departamento de {departamento}, República de Colombia.<br><br>**Cronograma general:**<br>El convenio se ejecutará conforme al cronograma establecido en la propuesta técnica, cumpliendo con los tiempos para:<br>• Fase de planeación: 10% del plazo<br>• Fase de ejecución: 70% del plazo<br>• Fase de socialización y entrega: 20% del plazo",

    "supervision": "Genera contenido sobre la supervisión del contrato:<br><br>La supervisión del presente convenio estará a cargo del funcionario designado por la Alcaldía Municipal de {municipio}, quien tendrá las siguientes funciones conforme al artículo 84 de la Ley 1474 de 2011:<br><br>**Funciones del supervisor:**<br>• Realizar seguimiento técnico, administrativo, financiero, contable y jurídico del convenio.<br>• Verificar el cumplimiento de las obligaciones contractuales.<br>• Aprobar los productos e informes entregados por el contratista.<br>• Suscribir las actas de inicio, seguimiento, suspensión y terminación.<br>• Solicitar las modificaciones contractuales que sean necesarias.<br>• Informar oportunamente sobre incumplimientos al ordenador del gasto.<br>• Certificar la ejecución para efectos de pago.<br><br>La supervisión se ejercerá de manera permanente durante el plazo de ejecución del convenio y hasta la liquidación del mismo."
}}

RECUERDA:
- Genera contenido EXTENSO y PROFESIONAL para cada sección
- USA el conocimiento normativo colombiano
- NO incluyas títulos de sección en el contenido (ya se agregan automáticamente)
- Todos los textos deben estar en español formal
- Para saltos de línea usa <br>
- Para viñetas usa •
- Para negritas usa **texto**
"""
