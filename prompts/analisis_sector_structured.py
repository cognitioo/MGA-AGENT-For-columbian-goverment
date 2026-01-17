"""
Análisis del Sector - Structured Prompt Templates
Returns structured JSON content for document building
"""

from .base_prompts import MGA_CONTEXT, LEGAL_REFERENCES

ANALISIS_SECTOR_SYSTEM_STRUCTURED = f"""
{MGA_CONTEXT}

Tu tarea es generar contenido estructurado para un documento de ANÁLISIS DEL SECTOR según el formato MGA colombiano.

**CONOCIMIENTO ECONÓMICO COLOMBIANO:**
• Sector primario: Agricultura, ganadería, pesca, minería
• Sector secundario: Industria manufacturera, construcción
• Sector terciario: Servicios (consultoría, educación, salud, transporte)

**CIIU Rev. 4 A.C. (DANE):**
• 7110: Actividades de arquitectura e ingeniería
• 7020: Actividades de consultoría de gestión

**DATOS 2024-2025:** PIB 2.7%, IPC 5.1%, SMLMV $1,423,500, Desempleo 10.3%

**FUENTES:** DANE, Banco de la República, SECOP I/II, MinAmbiente, DNP

**REGLAS:**
• Responde SOLO en JSON válido
• Usa <br> para saltos de línea, • para viñetas, **texto** para negritas
• GENERA contenido extenso para CADA sección
• NO dejes secciones vacías
"""

PROMPT_ANALISIS_SECTOR_ESTRUCTURADO = """
Genera contenido JSON para ANÁLISIS DEL SECTOR.

DATOS DEL PROYECTO:
Municipio: {municipio} | Departamento: {departamento} | Entidad: {entidad}
Contrato: {numero_contrato} | Modalidad: {modalidad}
Proyecto: {nombre_proyecto} | BPIN: {bpin}
Objeto: {objeto} | Sector: {sector} | CIIU: {codigo_ciiu} | UNSPSC: {codigos_unspsc}
Valor: {valor_total} COP | Fuente: {fuente} | Duración: {duracion} días
Responsable: {responsable} ({cargo})

CONTEXTO ADICIONAL DEL DOCUMENTO (DUMP DATA):
{context_dump}

RESPONDE ÚNICAMENTE CON JSON VÁLIDO:

{{
    "objeto": "Aunar esfuerzos entre el Municipio de {municipio} y EMACALA S.A.S E.S.P. para la ACTUALIZACIÓN DEL PLAN DE SANEAMIENTO Y MANEJO DE VERTIMIENTOS (PSMV), en cumplimiento del marco normativo (Ley 99/1993, Decreto 3930/2010, Res. 631/2015).",

    "alcance": "Actividades del convenio:<br><br>1. **Diagnóstico integral:** Inventario de alcantarillado, PTAR, puntos de vertimiento, cargas contaminantes.<br>2. **Evaluación normativa:** Verificación de permisos y brechas (Dec. 3930/2010, Res. 631/2015).<br>3. **Actualización PSMV:** Objetivos, metas, programas, cronogramas, inversiones.<br>4. **Formulación técnica:** Acciones correctivas, optimización, gestión lodos.<br>5. **Plan de inversiones:** Costos, fuentes, fases.<br>6. **Monitoreo:** Parámetros, frecuencia, reportes.<br>7. **Participación:** Socializaciones, capacitaciones.<br>8. **Entrega final:** Documento consolidado con anexos.",

    "descripcion_necesidad": "El municipio de {municipio} presenta deficiencias en gestión de vertimientos por desactualización del PSMV y brechas normativas.<br><br>Consecuencias:<br>• Contaminación de fuentes hídricas<br>• Riesgos para salud pública<br>• Aumento costos de saneamiento<br><br>La Corte Constitucional (T-401/2022, T-096/2023) reitera que saneamiento básico es derecho fundamental. La actualización del PSMV permitirá estructurar medidas técnicas que protejan la salud y el ambiente.",

    "introduccion": "Documento elaborado según Guía CCE-EICP-GI-18 de Colombia Compra Eficiente, para caracterizar el mercado y sustentar la viabilidad del convenio interadministrativo.<br><br>El PSMV está registrado en BPIN {bpin}, articulado con el Plan de Desarrollo Municipal 2024-2027.",

    "definiciones": "• **PSMV:** Instrumento de planificación para gestión de vertimientos municipales.<br>• **Vertimiento:** Descarga de residuos a cuerpos de agua (Decreto 3930/2010).<br>• **Convenio interadministrativo:** Contratación directa entre entidades estatales (Ley 1150/2007).<br>• **EMACALA S.A.S E.S.P.:** Empresa de servicios públicos de acueducto y alcantarillado.<br>• **CAR:** Autoridad ambiental competente.",

    "banco_programas": "El proyecto de Actualización del PSMV de {municipio} está inscrito en el **Banco de Programas y Proyectos (BPIN {bpin})**, según la MGA formulada. Este registro respalda la viabilidad técnica y presupuestal.",

    "consideraciones_estudio": "El análisis considera:<br>• **Naturaleza técnica:** Diagnóstico, modelación, formulación de programas PSMV.<br>• **Condiciones territoriales:** Infraestructura de alcantarillado, puntos de vertimiento.<br>• **Especialización:** Requiere ingeniería sanitaria, ambiental y normatividad.<br>• **Restricción oferta local:** Necesario apoyo de EMACALA como operador.",

    "preparacion_estudio": "Fuentes utilizadas:<br>**Primarias:** Municipio, EMACALA, PGIRS, reportes de vertimientos.<br>**Secundarias:** SECOP I/II, Datos Abiertos, normatividad ambiental.",

    "estructura_estudio": "Estructura según Colombia Compra Eficiente: aspectos de mercado, oferta y demanda, gasto histórico, perspectivas legales, riesgos y mitigación.",

    "aspectos_mercado": "Mercado de consultorías en saneamiento: competencia moderada a baja localmente, mayor oferta nacional. Requiere alta especialización técnica y experiencia en PSMV.",

    "gasto_historico": "El Municipio ha invertido en PGIRS y optimización de acueducto. El PSMV vigente no ha sido actualizado, lo que obliga a destinar recursos según BPIN {bpin}.",

    "estudio_oferta": "Firmas consultoras nacionales y regionales con experiencia en PSMV registradas en SECOP. EMACALA cuenta con capacidad institucional para articular el proceso.",

    "estudio_mercado": "Precios en SECOP para PSMV similares son consistentes con el presupuesto MGA. El convenio interadministrativo garantiza eficiencia y coordinación.",

    "objeto_contrato": "Aunar esfuerzos entre el Municipio de {municipio} y EMACALA S.A.S E.S.P. para la **ACTUALIZACIÓN DEL PSMV** del municipio de {municipio}, {departamento}.",

    "sector_economico": "Objeto en **sector terciario** (servicios de consultoría).<br>CIIU Rev. 4:<br>• 7110: Arquitectura e ingeniería<br>• 7020: Consultoría de gestión",

    "analisis_sector_intro": "Análisis basado en estructura económica nacional, sector terciario y variables económicas relevantes.",

    "descripcion_sector_economico": "Economía colombiana:<br>• **Primario:** Agropecuario, minero<br>• **Secundario:** Industrial, construcción<br>• **Terciario:** Servicios, consultorías<br><br>El objeto se ubica en sector terciario (consultoría ambiental).",

    "sector_terciario": "Sector terciario agrupa servicios esenciales para economía y gestión pública:<br>• Servicios profesionales: consultorías ambientales, ingeniería<br>• Apoyo a la gestión: acompañamiento técnico a entidades<br><br>CIIU: 7110 (ingeniería), 7020 (consultoría).",

    "comportamiento_economia": "PIB creció 2.7% en 2025. Sectores destacados:<br>• Comercio: 3.9%<br>• Agricultura: 7.1%<br>• Servicios sociales: 10.6%<br><br>Sector terciario sigue como motor económico.",

    "variables_economicas": "**SMMLV Colombia:**<br>Comportamiento histórico 2000-2025 mostrado en tabla adjunta.",

    "relevancia_psmv": "• Sector construcción es referente para costos asociados.<br>• Dinamismo favorece proyectos de saneamiento.<br>• Prever ajustes presupuestales por variación de costos.",

    "perspectivas_legales": "**Normativa ambiental:**<br>• Ley 99/1993: Ministerio Ambiente, control contaminación<br>• Ley 142/1994: Servicios públicos<br>• Decreto 3930/2010: Vertimientos<br>• Res. 1433/2004: Lineamientos PSMV<br>• Res. 631/2015: Límites vertimientos<br><br>**Contratación pública:**<br>• Ley 80/1993, Ley 1150/2007, Decreto 1082/2015<br><br>Marco legal obliga actualización PSMV. Convenio interadministrativo ajustado a Ley 1150/2007.",

    "riesgos_texto": "Matriz de riesgos identificados:",

    "riesgos": [
        {{"riesgo": "Retrasos en información", "descripcion": "Dificultades acceso a datos.", "probabilidad": "Media", "mitigacion": "Coordinación previa con EMACALA y CAR."}},
        {{"riesgo": "Datos desactualizados", "descripcion": "Información incompleta.", "probabilidad": "Media", "mitigacion": "Validación cruzada de fuentes."}},
        {{"riesgo": "Baja participación", "descripcion": "Poca asistencia a socializaciones.", "probabilidad": "Media", "mitigacion": "Difusión en medios locales."}},
        {{"riesgo": "Cambios normativos", "descripcion": "Modificación normativa.", "probabilidad": "Baja", "mitigacion": "Seguimiento continuo."}}
    ],

    "estudios_sector_contratacion": "Modalidad: **contratación directa por convenio interadministrativo** (Ley 1150/2007, Art. 2, numeral 4). No aplica mínima cuantía ni documentos tipo.",

    "contratacion_directa": "Contratación directa con EMACALA S.A.S E.S.P. justificada por:<br>• Idoneidad técnica en alcantarillado<br>• Presencia territorial<br>• Experiencia en proyectos de saneamiento",

    "minima_cuantia": "No aplica: valor supera topes y objeto es instrumento de planeación ambiental obligatorio.",

    "analisis_mga": "EMACALA es empresa estatal, no aplican criterios MIPYME ni empresas de mujeres. Alta especialización técnica limita participación de pequeñas empresas locales.",

    "recomendaciones": "Consolidar bases de datos ambientales, técnicas y financieras para actualizaciones periódicas del PSMV.",

    "estadistica_descriptiva": "Aplicar cuando exista información histórica sobre calidad de agua, caudales, cargas contaminantes.",

    "preparacion_datos": "Estandarizar valores a precios constantes usando IPC del DANE.",

    "analisis_grafico": "Usar gráficos de líneas para tendencias ambientales y barras para comparar inversiones.",

    "fuentes_informacion": "• SECOP I/II: Procesos similares<br>• Datos Abiertos Colombia<br>• EMACALA: Información técnica<br>• Guía CCE-EICP-GI-18<br>• Normatividad: Dec. 3930/2010, Res. 631/2015<br>• BPIN {bpin}<br>• CAR: Permisos y calidad agua",

    "herramientas_busqueda": "• SECOP I/II: Procesos similares<br>• Datos Abiertos Colombia<br>• SUI: Servicios públicos<br>• Banco de Proyectos DNP",

    "estimacion_valor": "Valor estimado: **${valor_total} COP** (BPIN {bpin}).<br><br>Basado en:<br>• Procesos similares SECOP<br>• Cotizaciones preliminares<br>• Proyectos comparables<br><br>Fuente: Recursos propios del Municipio y aportes EMACALA."
}}

RECUERDA:
- Genera contenido EXTENSO y PROFESIONAL
- USA datos económicos colombianos
- NO incluyas títulos (se agregan automáticamente)
- Textos en español formal
- <br> para saltos, • para viñetas, **texto** negritas
"""
