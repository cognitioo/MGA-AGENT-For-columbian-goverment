"""
Estudios Previos (Prior Studies) Prompt Templates
For generating MGA-compliant Prior Studies documents
"""

from .base_prompts import MGA_CONTEXT, LEGAL_REFERENCES

ESTUDIOS_PREVIOS_SYSTEM = f"""
{MGA_CONTEXT}

Tu tarea es generar secciones para un documento de ESTUDIOS PREVIOS según el formato MGA.
Los Estudios Previos son el documento técnico que justifica la necesidad del proyecto y define
las condiciones para su contratación.

{LEGAL_REFERENCES}

ESTRUCTURA DEL DOCUMENTO:
1. Encabezado con datos del contrato
2. Marco legal y normativo
3. Descripción de la necesidad
4. Objeto del convenio/contrato
5. Alcance y especificaciones técnicas
6. Obligaciones de las partes
7. Presupuesto estimado
8. Análisis de riesgos
9. Garantías exigidas
10. Plazo y lugar de ejecución
11. Supervisión
12. Firma del responsable
"""

# Section-specific prompts
PROMPT_DESCRIPCION_NECESIDAD = """
Genera la sección "DESCRIPCIÓN DE LA NECESIDAD" para un documento de Estudios Previos.

DATOS DEL PROYECTO:
- Municipio: {municipio}
- Departamento: {departamento}
- Tipo de proyecto: {tipo_proyecto}
- Problema identificado: {problema}
- Población beneficiaria: {poblacion}

INSTRUCCIONES:
1. Explica claramente el problema o necesidad que origina el proyecto
2. Incluye datos cuantitativos si están disponibles
3. Menciona las consecuencias de no atender la necesidad
4. Relaciona con los planes de desarrollo si es pertinente
5. Usa un tono técnico y formal

Genera SOLO esta sección, sin encabezados adicionales.
"""

PROMPT_OBJETO = """
Genera la sección "OBJETO DEL CONVENIO" para un documento de Estudios Previos.

DATOS:
- Tipo de objeto: {tipo_objeto}
- Descripción general: {descripcion}
- Entidades involucradas: {entidades}

INSTRUCCIONES:
1. Redacta el objeto de forma clara y concisa
2. Debe ser específico y medible
3. Incluye las entidades participantes si es un convenio interadministrativo
4. No incluyas el alcance aquí (eso va en otra sección)

Genera SOLO el texto del objeto.
"""

PROMPT_ALCANCE = """
Genera la sección "ALCANCE" para un documento de Estudios Previos.

OBJETO DEL PROYECTO: {objeto}

ACTIVIDADES A DESARROLLAR:
{actividades}

PRODUCTOS ESPERADOS:
{productos}

INSTRUCCIONES:
1. Lista las actividades principales que se desarrollarán
2. Especifica los productos o entregables
3. Define claramente los límites del alcance
4. Usa viñetas para mayor claridad

Genera la sección de alcance con formato de lista.
"""

PROMPT_PRESUPUESTO = """
Genera la sección "PRESUPUESTO ESTIMADO" para un documento de Estudios Previos.

VALOR TOTAL: {valor_total} COP
CÓDIGO BPIN: {bpin}

RUBROS:
{rubros}

FUENTE DE FINANCIACIÓN: {fuente}

INSTRUCCIONES:
1. Presenta el presupuesto en formato de tabla
2. Incluye todos los rubros con sus valores
3. El total debe coincidir con el valor indicado
4. Menciona la fuente de financiación
5. Si hay aportes de otras entidades, especifícalos

Genera la sección de presupuesto con tabla.
"""

PROMPT_RIESGOS = """
Genera la sección "ANÁLISIS DE RIESGOS" con matriz de riesgos.

TIPO DE PROYECTO: {tipo_proyecto}
SECTOR: {sector}
DURACIÓN: {duracion} días

RIESGOS IDENTIFICADOS (si los hay):
{riesgos_previos}

INSTRUCCIONES:
1. Identifica los principales riesgos del proyecto
2. Clasifica cada riesgo por tipo (técnico, financiero, legal, ambiental, operativo)
3. Evalúa probabilidad e impacto
4. Propón medidas de mitigación
5. Asigna responsable de cada riesgo

Genera una matriz de riesgos en formato tabla con columnas:
| Riesgo | Tipo | Probabilidad | Impacto | Mitigación |
"""

PROMPT_GARANTIAS = """
Genera la sección "ANÁLISIS QUE SUSTENTA LA EXIGENCIA DE GARANTÍAS".

VALOR DEL CONTRATO: {valor_total} COP
TIPO DE CONTRATO: {tipo_contrato}
DURACIÓN: {duracion} días

INSTRUCCIONES:
Genera los amparos exigidos según la normatividad colombiana:

a) Cumplimiento
   - Porcentaje del valor del contrato
   - Vigencia
   - Finalidad

b) Salarios, prestaciones sociales e indemnizaciones del personal
   - Porcentaje del valor del contrato
   - Vigencia
   
c) Responsabilidad civil extracontractual
   - Cuantía en SMLMV
   - Vigencia

d) Estabilidad de la obra (si aplica)
   - Porcentaje
   - Vigencia

Genera la sección con el formato especificado.
"""

PROMPT_SUPERVISION = """
Genera la sección "SUPERVISIÓN" para el documento de Estudios Previos.

ENTIDAD CONTRATANTE: {entidad}
DEPENDENCIA: {dependencia}

INSTRUCCIONES:
1. Indica que la supervisión estará a cargo de un funcionario designado
2. Lista las responsabilidades del supervisor:
   - Velar por el cumplimiento del objeto contractual
   - Revisar y aprobar informes
   - Certificar la correcta ejecución
   - Informar oportunamente sobre las novedades
   - Coordinar acciones necesarias

Genera la sección de supervisión siguiendo el formato oficial.
"""

# Complete document assembly prompt
PROMPT_ESTUDIOS_PREVIOS_COMPLETO = """
Genera un documento completo de ESTUDIOS PREVIOS con la siguiente información:

DATOS DEL PROYECTO:
- Municipio: {municipio}
- Departamento: {departamento}
- Entidad contratante: {entidad}
- Tipo de proyecto: {tipo_proyecto}
- Código BPIN: {bpin}

NECESIDAD:
{necesidad}

OBJETO:
{objeto}

ALCANCE Y ACTIVIDADES:
{alcance}

PRESUPUESTO:
- Valor total: {valor_total} COP
- Fuente: {fuente_financiacion}
- Rubros: {rubros}

INFORMACIÓN ADICIONAL:
- Plazo de ejecución: {plazo} días
- Lugar: {lugar}
- Responsable: {responsable}
- Cargo: {cargo}

Genera el documento completo siguiendo la estructura oficial de Estudios Previos para la MGA.
"""
