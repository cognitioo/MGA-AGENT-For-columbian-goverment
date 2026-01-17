"""
Análisis del Sector (Sector Analysis) Prompt Templates
For generating MGA-compliant Sector Analysis documents
"""

from .base_prompts import MGA_CONTEXT, LEGAL_REFERENCES

ANALISIS_SECTOR_SYSTEM = f"""
{MGA_CONTEXT}

Tu tarea es generar secciones para un documento de ANÁLISIS DEL SECTOR ECONÓMICO Y DE LOS OFERENTES
según el formato requerido por la MGA y Colombia Compra Eficiente.

Este documento analiza el contexto económico y de mercado para justificar las decisiones de contratación.

{LEGAL_REFERENCES}

LEY ESPECÍFICA:
- El análisis del sector se enmarca en el numeral 4 del artículo 2 de la Ley 1150 de 2007

ESTRUCTURA DEL DOCUMENTO:
1. Datos del contrato
2. Objeto y alcance
3. Descripción de la necesidad
4. Desarrollo del estudio del sector
5. Análisis económico y del mercado
6. Variables económicas (PIB, IPC, empleo)
7. Análisis de riesgos
8. Estimación y justificación del valor
9. Fuentes de información
10. Firma del responsable
"""

PROMPT_DESARROLLO_ESTUDIO = """
Genera la sección "DESARROLLO DEL ESTUDIO DEL SECTOR" incluyendo:

DATOS DEL PROYECTO:
- Nombre del proyecto: {nombre_proyecto}
- Código BPIN: {bpin}
- Plan de Desarrollo relacionado: {plan_desarrollo}
- Sector: {sector}

INSTRUCCIONES:

1.1 Banco de Programas y Proyectos
- Menciona el registro en el Banco de Programas y Proyectos de Inversión Nacional
- Incluye el código BPIN
- Relaciona con el Plan de Desarrollo Municipal

1.2 Definiciones
- Define los términos técnicos relevantes al sector
- Incluye definiciones normativas si aplican

1.3 Preparación del Estudio
- Lista las fuentes de información consultadas:
  * Información administrativa del municipio
  * SECOP I y II
  * Datos Abiertos Colombia (DANE)
  * Proyectos similares en otros municipios

Genera estas secciones con formato estructurado.
"""

PROMPT_ESTRUCTURA_ESTUDIO = """
Genera la sección "ESTRUCTURA DEL ESTUDIO DEL SECTOR" con:

DATOS:
- Objeto del contrato: {objeto}
- Sector económico: {sector}

INSTRUCCIONES:
Genera las siguientes subsecciones:

1.4.1 Aspectos generales del mercado
- Descripción del mercado relevante
- Nivel de competencia

1.4.2 Componente del gasto
- Clasificación del gasto

1.4.3 Clasificación UNSPSC
- Código(s) UNSPSC aplicables: {codigos_unspsc}

1.4.4 Objeto del contrato
- Descripción clara del objeto

1.4.5 Sector económico de la necesidad
- Clasificación CIIU Rev. 4 A.C.: {codigo_ciiu}
- Descripción del sector según DANE

Genera estas secciones de forma concisa y técnica.
"""

PROMPT_ANALISIS_ECONOMICO = """
Genera la sección "ANÁLISIS DEL SECTOR" con análisis económico.

SECTOR: {sector}
AÑO DE REFERENCIA: {ano}
DEPARTAMENTO: {departamento}

INSTRUCCIONES:

1.5.1 Descripción del sector económico
- Explica los tres sectores de la economía (primario, secundario, terciario)
- Ubica el proyecto en el sector correspondiente (generalmente terciario para servicios)

1.5.2 Comportamiento de la economía
- Menciona el crecimiento del PIB (usar datos generales de Colombia)
- Referencia el comportamiento del sector específico
- Cita fuente: DANE

1.5.3 Variables económicas
- Incluye referencia a:
  * Salario mínimo vigente
  * IPC (Índice de Precios al Consumidor)
  * Tendencias del mercado laboral

NOTA: No inventes cifras específicas. Usa referencias generales y sugiere consultar fuentes oficiales.

Genera el análisis económico con formato estructurado.
"""

PROMPT_RIESGOS_SECTOR = """
Genera la sección de RIESGOS Y PERSPECTIVAS para el análisis del sector.

TIPO DE PROYECTO: {tipo_proyecto}
VALOR ESTIMADO: {valor} COP
DURACIÓN: {duracion} días

INSTRUCCIONES:
Genera una matriz con los siguientes tipos de riesgos:

| Tipo de Riesgo | Descripción | Mitigación |
|----------------|-------------|------------|
| Perspectiva comercial | Riesgos de mercado | Medidas |
| Perspectiva financiera | Riesgos presupuestales | Medidas |
| Perspectiva organizacional | Riesgos de coordinación | Medidas |
| Perspectiva técnica | Riesgos metodológicos | Medidas |

Incluye riesgos específicos como:
- Inconsistencias en la información base
- Cambios normativos
- Baja participación comunitaria
- Limitaciones presupuestales
- Retrasos en aprobaciones

Genera la matriz completa.
"""

PROMPT_ESTIMACION_VALOR = """
Genera la sección "ESTIMACIÓN Y JUSTIFICACIÓN DEL VALOR DEL CONTRATO".

DATOS:
- Valor estimado: {valor_total} COP
- Código BPIN: {bpin}
- Objeto: {objeto}

FUENTES DE LA ESTIMACIÓN:
{fuentes_estimacion}

FUENTE DE FINANCIACIÓN:
{fuente_financiacion}

INSTRUCCIONES:
1. Presenta el valor estimado
2. Justifica cómo se llegó a ese valor:
   - Procesos similares en SECOP
   - Cotizaciones preliminares
   - Experiencia en proyectos comparables
3. Indica la fuente de financiación
4. Menciona aportes de otras entidades si aplica

Genera la sección de estimación del valor.
"""

PROMPT_FUENTES_INFORMACION = """
Genera la sección "FUENTES DE INFORMACIÓN" para el análisis del sector.

SECTOR: {sector}
MUNICIPIO: {municipio}
DEPARTAMENTO: {departamento}

INSTRUCCIONES:
Lista las fuentes de información utilizadas:

1. SECOP I y II
   - Búsqueda de procesos similares
   - Análisis de consultorías

2. Datos Abiertos Colombia / DANE
   - Estadísticas poblacionales
   - Indicadores económicos

3. Documentación municipal
   - Planes de desarrollo
   - Proyectos anteriores
   - PGIRS, PSMV según aplique

4. Catálogo UNSPSC
   - Clasificación de bienes y servicios

5. MGA Web / BPIN
   - Registro de proyectos

6. Normatividad
   - Decretos y resoluciones del sector

Genera la lista de fuentes organizada.
"""

# Complete document prompt
PROMPT_ANALISIS_SECTOR_COMPLETO = """
Genera un documento completo de ANÁLISIS DEL SECTOR con la siguiente información:

DATOS DEL CONTRATO:
- Número: {numero_contrato}
- Modalidad: {modalidad}
- Municipio: {municipio}
- Departamento: {departamento}
- Entidad: {entidad}

PROYECTO:
- Nombre: {nombre_proyecto}
- BPIN: {bpin}
- Objeto: {objeto}
- Sector: {sector}
- Código CIIU: {codigo_ciiu}
- Códigos UNSPSC: {codigos_unspsc}

PRESUPUESTO:
- Valor total: {valor_total} COP
- Fuente de financiación: {fuente}

PLAZOS:
- Duración: {duracion} días

RESPONSABLE:
- Nombre: {responsable}
- Cargo: {cargo}

Genera el documento completo de Análisis del Sector siguiendo la estructura oficial.
"""
