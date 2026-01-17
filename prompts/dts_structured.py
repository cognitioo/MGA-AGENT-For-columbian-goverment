"""
DTS (Documento Técnico de Soporte) Structured Prompt Templates
Technical Support Document for MGA projects
"""

from .base_prompts import MGA_CONTEXT

DTS_SYSTEM_STRUCTURED = f"""
{MGA_CONTEXT}

Tu tarea es generar contenido estructurado para un DOCUMENTO TÉCNICO DE SOPORTE (DTS) según el formato MGA colombiano.

**ESTRUCTURA DTS:**
El DTS es un documento técnico que soporta proyectos de inversión pública, especialmente para servicios públicos domiciliarios (acueducto, alcantarillado, aseo).

**SECCIONES PRINCIPALES:**
1. Contribución a la Política Pública (planes de desarrollo)
2. Identificación y Descripción del Problema
3. Problema Central e Indicadores
4. Análisis de Participantes
5. Poblaciones Afectadas
6. Estudio de Necesidades (Oferta/Demanda)
7. Alternativas de Solución
8. Cadena de Valor
9. Fuentes de Financiación

**REGLAS:**
• Responde SOLO en JSON válido
• Usa <br> para saltos de línea, • para viñetas, **texto** para negritas
• Genera contenido técnico y profesional
• Incluye datos numéricos realistas
• NO dejes secciones vacías
"""

PROMPT_DTS_ESTRUCTURADO = """
Genera contenido para un DOCUMENTO TÉCNICO DE SOPORTE (DTS) para proyecto de inversión pública.

DATOS DEL PROYECTO:
Municipio: {municipio} | Departamento: {departamento}
Entidad: {entidad} | BPIN: {bpin}
Proyecto: {nombre_proyecto}
Objeto: {objeto}
Valor: {valor_total} COP | Duración: {duracion} días
Responsable: {responsable} ({cargo})
Programa: {programa} | Subprograma: {subprograma}

CONTEXTO ADICIONAL DEL DOCUMENTO (DUMP DATA):
{context_dump}

RESPONDE ÚNICAMENTE CON JSON VÁLIDO:

{{
    "titulo_proyecto": "SUBSIDIO DE SERVICIOS PÚBLICOS DOMICILIARIOS DE ACUEDUCTO, ALCANTARILLADO Y ASEO PARA LA POBLACIÓN VULNERABLE DEL MUNICIPIO DE {municipio}",

    "contribucion_plan_nacional": "• **PLAN:** 2022-2026 Colombia Potencia Mundial de la Vida<br>• **PACTO/PILAR:** XII - Convergencia regional<br>• **TRANSFORMACIÓN:** 1 - Ordenamiento del territorio alrededor del agua y justicia ambiental<br>• **PLAN:** 31 - Ecuador biodiverso, asegurar agua y crear condiciones para aprovechamiento económico bajo un ordenamiento territorial bajo modelo de conocimiento.<br>• **CUALIFICACIÓN:** 82 - El agua, la biodiversidad y los recursos, a la agenda del ordenamiento de vida territorial<br>• **COMPONENTE:** 3 - Agua para la vida, ecosistemas saludables para la vida",

    "contribucion_plan_departamental": "• **PLAN:** 2024-2027 {departamento}<br>• **ESTRATEGIA:** 2 - Línea de Bienestar Con Justicia Social - Como De Derechos Y Calidad De Vida Para Todos<br>• **META TRANSFORMACIÓN:** Desarrollo Humano.<br>• **PROGRAMA:** 4.0.5 - Viviendas 10 de Servicios Públicos - APyS - Acercar de la población a los servicios de agua potable y saneamiento básico",

    "contribucion_plan_municipal": "• **PLAN:** 2024-2027 {municipio} Mejor<br>• **ESTRATEGIA:** Agua de vida con Identidad Bolivarense<br>• **PROGRAMA:** 4002 - Usuarios beneficiados con subsidios al consumo del servicio de acueducto<br>• **Línea base:** 6914<br>• **Meta de cuatrienio:** 8473<br><br>• **PROGRAMA:** Usuarios beneficiados con subsidios al consumo del servicio de alcantarillado<br>• **Línea base:** 6171<br>• **Meta de cuatrienio:** 6422",

    "descripcion_situacion_actual": "El marco de subsidios del CCP APSB está orientado a corregir asimetrías en el acceso a los servicios básicos como el resultado de la desigualdad en la capacidad o disposición de pago por los servicios, considerando los niveles de pobreza y vulnerabilidad. El diseño actual de la 2005 v 0624 del 2011, compilados en la el Decreto 1077 de 2015, dispone la inversibilidad, obligando al otorgamiento de subsidios desde el Estado para que los usuarios con dificultad para el pago pueda cumplir con todos sus compromisos.<br><br>• Considerados los costes de los ítemes internos correspondientes a los artículos 1 y 2 según la metodología plenamente adoctada por la entidad territorial.<br><br>• El gobierno nacional consolidó financiación acorde a distintos lineamientos para atacar costos de operación y mantenimiento de los suministros, estos son calculados de acuerdo a modelos del artículo 125 de la ley 1450 de 2011, aplicable que sea justificado.",

    "problema_central": "Falta cobertura y baja calidad del servicio de Acueducto, Alcantarillado y Aseo en la zona urbana del municipio.",

    "magnitud_problema": "Garantizar los subsidios al consumo que están actualmente adjudicados manteniendo los niveles de los usuarios 1 y 2 cuyos usuarios podrían no cumplir con todos los requerimientos, así como 57591 claro 5000, beneficiarios, 02 584 beneficiarios. Actualmente total de usuarios: 3.384 (El 2-448 (Acu.: 2 727 Alc.: 2 671 Aseo: 3.384)).",

    "causas_directas": "• Disminución de los pagos de cartera corriente por concepto de los servicios públicos domiciliarios (Estrato 1 y 2)<br>• Disminución de recursos para garantizar la continuidad del servicio",

    "efectos_directos": "• Deterioro de la calidad del servicio de Acueducto, Alcantarillado y Aseo<br>• Disminución en la cobertura del servicio<br>• Menor calidad de vida para la población vulnerable",

    "analisis_participantes": [
        {{"actor": "San Pablo - Bolívar", "entidad": "Generador y resolutor: Garantizar suficiente recursos básicos de los usuarios 1 y 2", "posicion": "Cooperante", "tipo": "Beneficiario"}},
        {{"actor": "EMACALA E.S.P S.A.S", "entidad": "Dar cumplimiento a la aplicabilidad en el manejo del 54 del abril 43 del 1984", "posicion": "Cooperante", "tipo": "Beneficiario"}},
        {{"actor": "Usuarios estratos 1 y 2", "entidad": "Tener beneficios, permanecer, segui económico", "posicion": "Beneficiario", "tipo": "Beneficiario"}}
    ],

    "poblacion_afectada": "Personas",
    "localizacion": "{municipio}, {departamento}",

    "poblacion_objetivo": "Transferir los recursos de subsidio para los consumos públicos colectivas de Acueducto, Alcantarillado y Aseo a la EMACALA E.S.P S.A.S",

    "desarrollo_alternativa": "Los subsidios corresponden al porcentaje establecido por la Resolución Nacional, con aplicación a la Gestión Pública y a la ley, y busca dar aporte máximo de revisar, representar con la oferta de los costos de acueducto, alcantarillado y aseo. Por la giga, la presentación de las inversiones públicas serán apalancados, no recuperar, ejercer el servicio, impuesto de la manera del detrimento.<br><br>El artículo a la tarifa para los servicios públicos domiciliarios de Acueducto, Alcantarillado y Aseo se acogería a los usuarios de los servicios del estrato 1 y 2 de acuerdo con la normatividad recientemente a efectivo correspondiente al municipio.",

    "objetivo_general": "Garantizar el servicio de acueducto y alcantarillado a la población de estratos 1 y 2 del municipio de {municipio}, cubriendo los porcentajes del subsidio definidos por el gobierno.",

    "objetivo_especifico": "Hacer más eficiente el subsidio, el objetivo es mejorar.",

    "tabla_subsidios_acueducto": [
        {{"ano": "2021", "oferta": "5,440.00", "demanda": "5,440.00", "deficit": "0.00"}},
        {{"ano": "2022", "oferta": "5,513.00", "demanda": "5,513.00", "deficit": "0.00"}},
        {{"ano": "2023", "oferta": "5,588.00", "demanda": "5,588.00", "deficit": "0.00"}},
        {{"ano": "2024", "oferta": "5,588.00", "demanda": "5,588.00", "deficit": "0.00"}},
        {{"ano": "2025", "oferta": "0.00", "demanda": "5,700.00", "deficit": "-5,700.00"}},
        {{"ano": "2026", "oferta": "0.00", "demanda": "5,700.00", "deficit": "-5,700.00"}},
        {{"ano": "2027", "oferta": "0.00", "demanda": "5,700.00", "deficit": "-5,700.00"}}
    ],

    "tabla_subsidios_alcantarillado": [
        {{"ano": "2021", "oferta": "2,725.00", "demanda": "2,725.00", "deficit": "0.00"}},
        {{"ano": "2022", "oferta": "2,748.00", "demanda": "2,748.00", "deficit": "0.00"}},
        {{"ano": "2023", "oferta": "2,771.00", "demanda": "2,771.00", "deficit": "0.00"}},
        {{"ano": "2024", "oferta": "2,775.00", "demanda": "2,775.00", "deficit": "0.00"}},
        {{"ano": "2025", "oferta": "0.00", "demanda": "3,084.00", "deficit": "-3,084.00"}},
        {{"ano": "2026", "oferta": "0.00", "demanda": "3,084.00", "deficit": "-3,084.00"}},
        {{"ano": "2027", "oferta": "0.00", "demanda": "3,084.00", "deficit": "-3,084.00"}}
    ],

    "tabla_subsidios_aseo": [
        {{"ano": "2021", "oferta": "5,557.00", "demanda": "5,557.00", "deficit": "0.00"}},
        {{"ano": "2022", "oferta": "5,634.00", "demanda": "5,634.00", "deficit": "0.00"}},
        {{"ano": "2023", "oferta": "5,711.00", "demanda": "5,711.00", "deficit": "0.00"}},
        {{"ano": "2024", "oferta": "5,711.00", "demanda": "5,711.00", "deficit": "0.00"}},
        {{"ano": "2025", "oferta": "0.00", "demanda": "5,681.00", "deficit": "-5,681.00"}},
        {{"ano": "2026", "oferta": "0.00", "demanda": "5,681.00", "deficit": "-5,681.00"}},
        {{"ano": "2027", "oferta": "0.00", "demanda": "5,681.00", "deficit": "-5,681.00"}}
    ],

    "cadena_valor_productos": [
        {{
            "codigo": "7.1",
            "producto": "Servicio de apoyo financiero para subsidio al consumo de servicios públicos domiciliarios",
            "medida": "Número de usuarios",
            "cantidad": "5,700,000",
            "costo": "$1,200,532,612.64"
        }},
        {{
            "codigo": "7.1.1",
            "actividad": "Realizar el pago de los aportes para subsidiar a los usuarios de los servicios públicos domiciliarios de Acueducto de los estratos uno (1) y dos (2) del municipio de {municipio}, Bolívar",
            "etapa": "Inversión",
            "costo": "$563,623,133.51"
        }},
        {{
            "codigo": "7.1.2",
            "actividad": "Realizar el pago de los aportes para subsidiar a los usuarios de los servicios públicos domiciliarios de Alcantarillado de los estratos uno (1) y dos (2) del municipio de {municipio}, Bolívar",
            "etapa": "Inversión",
            "costo": "$160,369,510.22"
        }},
        {{
            "codigo": "7.1.3",
            "actividad": "Realizar el pago de los aportes para subsidiar a los usuarios de los servicios públicos domiciliarios de Aseo de los estratos uno (1) y dos (2) del municipio de {municipio}, Bolívar",
            "etapa": "Inversión",
            "costo": "$446,540,168.91"
        }}
    ],

    "fuente_financiacion": "Recursos SGP - APSB",
    "total_recursos": "{valor_total}",

    "indicadores": [
        {{"objetivo": "Número", "meta": "6,000"}},
        {{"objetivo": "Estrato 1: Acueducto", "meta": "50%"}},
        {{"objetivo": "Estrato 2: Acueducto", "meta": "40%"}},
        {{"objetivo": "Tarifa base 12,772 m³", "meta": "50%"}},
        {{"objetivo": "Servicio de Alcantarillado para Estrato 1", "meta": "2,45%"}},
        {{"objetivo": "Servicio de Aseo", "meta": "$471"}}
    ]
}}

RECUERDA:
- Genera contenido TÉCNICO y PROFESIONAL
- Incluye datos numéricos realistas
- Todos los textos en español formal
- Para saltos de línea usa <br>
- Para viñetas usa •
- Para negritas usa **texto**
"""
