"""
MGA Subsidios Document Structured Prompt Templates
Full MGA document for subsidies projects (24 pages)
"""

from .base_prompts import MGA_CONTEXT

MGA_SUBSIDIOS_SYSTEM = f"""
{MGA_CONTEXT}

Tu tarea es generar contenido estructurado para un documento MGA COMPLETO (Metodología General Ajustada) para proyectos de subsidios de servicios públicos.

**ESTRUCTURA MGA SUBSIDIOS (24 páginas):**
Este documento sigue el formato oficial del DNP para registro de proyectos de inversión.

**SECCIONES:**
1. Datos Básicos del Proyecto
2. Contribución a la Política Pública (Plan Nacional, Departamental, Municipal)
3. Identificación y Descripción del Problema
4. Causas y Efectos del Problema
5. Participantes
6. Población (próximas páginas)
7. Objetivos (próximas páginas)
8. Alternativas (próximas páginas)
9. Indicadores (próxomas páginas)
10. Cadena de Valor (próximas páginas)
... (más secciones)

**⚠️ REGLAS CRÍTICAS DE PRECISIÓN DE DATOS:**
• NUNCA inventes datos, valores, números, nombres o fechas
• Si un dato NO está disponible en el contexto, usa "N/A" o "Por definir"
• USA ÚNICAMENTE los datos proporcionados en DATOS DEL PROYECTO y CONTEXTO ADICIONAL
• Para valores numéricos faltantes, usa "0" o "N/A" 
• Para textos faltantes, usa "N/A" o "Información no disponible"
• El municipio, departamento, valor y responsable DEBEN ser los proporcionados
• NO uses valores de ejemplo como "30.104" o "Juan Pérez" si no están en el contexto

**REGLAS GENERALES:**
• Responde SOLO en JSON válido
• Usa lenguaje técnico y formal
• Mantén consistencia con el formato MGA
"""

PROMPT_MGA_SUBSIDIOS_PAGINAS_1_5 = """
Genera contenido para las PRIMERAS 5 PÁGINAS del documento MGA Subsidios.

DATOS DEL PROYECTO:
Municipio: {municipio} | Departamento: {departamento}
Entidad: {entidad} | BPIN: {bpin}
Proyecto: "{nombre_proyecto}"
Valor: ${valor_total} COP | Duración: {duracion} días
Responsable: {responsable} ({cargo})
Identificador: {identificador}
Fecha creación: {fecha_creacion}

DATOS PLANES DE DESARROLLO:
Plan Nacional: {plan_nacional}
Plan Departamental: {plan_departamental}
Plan Municipal: {plan_municipal}

CONTEXTO ADICIONAL DEL DOCUMENTO (DUMP DATA):
{context_dump}

RESPONDE CON JSON VÁLIDO:

{{
    "pagina_1_datos_basicos": {{
        "titulo_documento": "CONTRIBUCIÓN AL ACCESO EQUITATIVO Y SOSTENIDO A LOS SERVICIOS PÚBLICOS DOMICILIARIOS DE ACUEDUCTO, ALCANTARILLADO Y ASEO MEDIANTE EL OTORGAMIENTO DE SUBSIDIOS AL CONSUMO PARA LA POBLACIÓN DE LOS ESTRATOS 1 Y 2 DEL MUNICIPIO DE {municipio}, GARANTIZANDO LA COBERTURA DE NECESIDADES BÁSICAS Y MEJORANDO SU CALIDAD DE VIDA. {municipio}",
        "nombre": "Contribución al acceso equitativo y sostenido a los servicios públicos domiciliarios de acueducto, alcantarillado y aseo mediante el otorgamiento de subsidios al consumo para la población de los estratos 1 y 2 del municipio de {municipio}, garantizando la cobertura de necesidades básicas y mejorando su calidad de vida. {municipio}",
        "tipologia": "A - PIIP - Bienes y Servicios",
        "codigo_bpin": "{bpin}",
        "sector": "Vivienda, ciudad y territorio",
        "es_proyecto_tipo": "No",
        "fecha_creacion": "{fecha_creacion}",
        "identificador": "{identificador}",
        "formulador_ciudadano": "{responsable}",
        "formulador_oficial": "{responsable}"
    }},

    "pagina_2_plan_desarrollo": {{
        "plan_nacional": {{
            "nombre": "(2022-2026) Colombia Potencia Mundial de la Vida",
            "programa": "4003 - Acceso de la población a los servicios de agua potable y saneamiento básico",
            "transformacion": "1. Ordenamiento de territorio alrededor del agua y justicia ambiental",
            "pilar": "01. Consolidar la base natural, cultural y arqueológica del territorio como los elementos primarios del ordenamiento territorial, bajo un enfoque de justicia ambiental orientado al desarrollo sostenible.",
            "catalizador": "02. El agua, la biodiversidad y las personas, en el centro del ordenamiento territorial",
            "componente": "a. Ciclo del agua como base del ordenamiento territorial"
        }},
        "plan_departamental": {{
            "nombre": "Bolívar Me Enamora 2024-2027",
            "estrategia": "Línea Bolívar Me Enamora con Justicia Social: Cierre de Brechas y Calidad de Vida para Todos.",
            "programa": "2.1.3 Programa de Servicios Públicos"
        }},
        "plan_municipal": {{
            "nombre": "{plan_municipal}",
            "estrategia": "Eje Estratégico 3: Desarrollo social para el bienestar y la felicidad",
            "programa": "4003 - Acceso de la población a los servicios de agua potable y saneamiento básico"
        }},
        "instrumentos_grupos_etnicos": "No aplica"
    }},

    "pagina_3_problematica": {{
        "problema_central": "Limitado acceso y deficiente cobertura en los servicios públicos domiciliarios de acueducto, alcantarillado y aseo para la población vulnerable de los estratos 1 y 2 del municipio de {municipio}, lo que impide la satisfacción de sus necesidades básicas.",
        "descripcion_situacion": "El municipio de {municipio} presenta limitaciones estructurales en la cobertura y calidad de los servicios públicos domiciliarios de acueducto, alcantarillado y aseo, especialmente en los estratos 1 y 2, que conforman la mayor parte de la población urbana vulnerable. De acuerdo con la información reportada, el servicio de acueducto cubre aproximadamente 5.748 usuarios (5.101 del estrato 1 y 647 del estrato 2), el alcantarillado 3.044 usuarios (2.444 del estrato 1 y 600 del estrato 2), y el aseo 5.699 usuarios (5.047 del estrato 1 y 652 del estrato 2).\\n\\nEl acceso a estos servicios básicos se ve afectado por las condiciones socioeconómicas de los usuarios, quienes requieren del otorgamiento de subsidios financiados por el municipio a través del SGP-APSB. La asignación de subsidios debe cumplir con los requisitos establecidos en la Ley 142 de 1994 y el Decreto 1077 de 2015, que obligan a que los beneficiarios estén debidamente identificados y que los subsidios no excedan los porcentajes autorizados por el Concejo Municipal. Sin embargo, actualmente se evidencia una distribución no óptima de estos recursos, lo que genera inequidades y dificultades en el pago oportuno de los servicios por parte de la población más vulnerable.",
        "magnitud_problema": "El municipio de {municipio} presenta limitaciones estructurales en la cobertura y calidad de los servicios públicos domiciliarios de acueducto, alcantarillado y aseo, especialmente en los estratos 1 y 2, que conforman la mayor parte de la población urbana vulnerable. De acuerdo con la información reportada, el servicio de acueducto cubre aproximadamente 5.748 usuarios (5.101 del estrato 1 y 647 del estrato 2), el alcantarillado 3.044 usuarios (2.444 del estrato 1 y 600 del estrato 2), y el aseo 5.699 usuarios (5.047 del estrato 1 y 652 del estrato 2).\\n\\nEl acceso a estos servicios básicos se ve afectado por las condiciones socioeconómicas de los usuarios, quienes requieren del otorgamiento de subsidios financiados por el municipio a través del SGP-APSB."
    }},

    "pagina_4_causas_efectos": {{
        "causas_directas": [
            {{"numero": "1", "causa": "Deficiente identificación de la población subsidiable en los estratos 1 y 2."}}
        ],
        "causas_indirectas": [
            {{"numero": "1.1", "causa": "Inadecuada distribución de los recursos destinados a subsidios."}}
        ],
        "efectos_directos": [
            {{"numero": "1", "efecto": "Desigualdad en los pagos de los servicios públicos domiciliarios según el estrato socioeconómico."}}
        ],
        "efectos_indirectos": [
            {{"numero": "1.1", "efecto": "Aumento en las tarifas de los servicios públicos domiciliarios para la población vulnerable."}}
        ]
    }},

    "pagina_5_participantes": {{
        "participantes": [
            {{
                "actor": "Municipal",
                "entidad": "SAN PABLO - BOLÍVAR",
                "posicion": "Cooperante",
                "intereses": "Cumplimiento del PDM, garantizar acceso equitativo a servicios públicos.",
                "contribucion": "Financiación, ejecución, supervisión y gestión presupuestal."
            }},
            {{
                "actor": "Otro",
                "entidad": "EMACALA S.A.S E.S.P",
                "posicion": "Beneficiario",
                "intereses": "Mejorar cartera, cobertura y sostenibilidad financiera.",
                "contribucion": "Facturación y aplicación efectiva de los subsidios."
            }},
            {{
                "actor": "Otro",
                "entidad": "COMUNIDAD",
                "posicion": "Beneficiario",
                "intereses": "Reducción del costo del servicio, acceso garantizado.",
                "contribucion": "Participación en socialización y veeduría ciudadana."
            }}
        ],
        "analisis_participantes": "La formulación del proyecto ha contado con espacios de consulta interna y coordinación interinstitucional, liderados por la Alcaldía de {municipio} a través de la Secretaría de Planeación y la dependencia encargada de los servicios públicos.\\n\\nSe ha mantenido diálogo técnico con la empresa prestadora del servicio EMACALA S.A.S E.S.P., con el fin de identificar los usuarios potenciales de subsidio, revisar la cobertura de los estratos 1 y 2, y validar la estructura tarifaria. Esta coordinación garantiza que la aplicación de los subsidios se realice conforme a la normatividad vigente y con criterios de sostenibilidad financiera.\\n\\nAsimismo, se han desarrollado mecanismos de socialización con la comunidad a través de encuentros participativos y veedurías ciudadanas, permitiendo recoger sus expectativas frente al acceso, calidad y costo del servicio. Estos aportes han sido fundamentales para la definición de prioridades del proyecto y la validación de la población beneficiaria.\\n\\nEn su fase de ejecución, se mantendrá una articulación constante con estos actores, garantizando la trazabilidad del proyecto, su seguimiento y evaluación participativa, conforme a los lineamientos del PDM y el marco del SGP."
    }}
}}
"""

PROMPT_MGA_SUBSIDIOS_PAGINAS_6_11 = """
Genera contenido para las PÁGINAS 6-11 del documento MGA Subsidios.

DATOS DEL PROYECTO:
Municipio: {municipio} | Departamento: {departamento}
Proyecto: "{nombre_proyecto}"
Valor: ${valor_total} COP

RESPONDE CON JSON VÁLIDO:

{{
    "pagina_6_poblacion": {{
        "poblacion_afectada": {{
            "tipo": "Personas",
            "numero": "30.104",
            "fuente": "Sistema Universo - EMACALA S.A.S E.S.P S.A.S con corte a enero de 2026",
            "region": "Caribe",
            "departamento": "{departamento}",
            "municipio": "{municipio}"
        }},
        "poblacion_objetivo": {{
            "tipo": "Personas",
            "numero": "30.104",
            "fuente": "Sistema Universo - EMACALA S.A.S E.S.P S.A.S con corte a enero de 2026",
            "region": "Caribe",
            "departamento": "{departamento}",
            "municipio": "{municipio}"
        }}
    }},

    "pagina_7_objetivos": {{
        "problema_central": "Limitado acceso y deficiente cobertura en los servicios públicos domiciliarios de acueducto, alcantarillado y aseo para la población vulnerable de los estratos 1 y 2 del municipio de {municipio}, lo que impide la satisfacción de sus necesidades básicas.",
        "objetivo_general": "Mejorar el acceso equitativo a los servicios públicos domiciliarios de acueducto, alcantarillado y aseo mediante el otorgamiento de subsidios a la población vulnerable de los estratos 1 y 2 del municipio de {municipio}.",
        "indicadores": [
            {{
                "nombre": "Familias subsidiadas en cobertura de Acueducto",
                "medido": "Número",
                "meta": "6.332",
                "tipo_fuente": "Documento oficial",
                "fuente_verificacion": "EMACALA S.A.S E.S.P y Secretaría de Planeación"
            }}
        ],
        "relacion_causas_objetivos": [
            {{
                "causa": "Causa directa 1: Deficiente identificación de la población subsidiable en los estratos 1 y 2.",
                "objetivo": "Identificar y focalizar adecuadamente la población usuaria de los estratos 1 y 2 con derecho a subsidio en los servicios públicos domiciliarios."
            }},
            {{
                "causa": "Causa indirecta 1.1: Inadecuada distribución de los recursos destinados a subsidios.",
                "objetivo": "Distribuir eficiente y equitativamente los recursos destinados a subsidios, conforme a los criterios técnicos y normativos."
            }}
        ],
        "alternativas": [
            {{
                "nombre": "Transferir los recursos de subsidios para los servicios públicos domiciliarios de Acueducto, Alcantarillado y Aseo a la EMACALA S.A.S E.S.P",
                "evaluacion": "Si",
                "estado": "Completo"
            }}
        ],
        "evaluaciones": {{
            "rentabilidad": "Si",
            "costo_eficiencia": "Si",
            "multicriterio": "No"
        }}
    }},

    "pagina_8_9_10_11_estudio_necesidades": {{
        "aseo": {{
            "bien_servicio": "Apoyo financiero para los usuarios de servicios públicos domiciliarios de aseo en los estratos 1 y 2.",
            "medido": "Número",
            "descripcion": "Apoyo financiero para los usuarios de servicios públicos domiciliarios de aseo en los estratos 1 y 2.",
            "descripcion_demanda": "Corresponde a la cantidad de subsidios que se requiere otorgar para satisfacer necesidades básicas para los usuarios de servicios públicos domiciliarios de aseo en los estratos 1 y 2.",
            "descripcion_oferta": "Corresponde a la cantidad de subsidios que se otorgan.",
            "tabla_oferta_demanda": [
                {{"ano": "2021", "oferta": "5.557,00", "demanda": "5.557,00", "deficit": "0,00"}},
                {{"ano": "2022", "oferta": "5.634,00", "demanda": "5.634,00", "deficit": "0,00"}},
                {{"ano": "2023", "oferta": "5.711,00", "demanda": "5.711,00", "deficit": "0,00"}},
                {{"ano": "2024", "oferta": "5.711,00", "demanda": "5.711,00", "deficit": "0,00"}},
                {{"ano": "2025", "oferta": "5.699,00", "demanda": "5.699,00", "deficit": "0,00"}},
                {{"ano": "2026", "oferta": "0,00", "demanda": "5.699,00", "deficit": "-5.699,00"}},
                {{"ano": "2027", "oferta": "0,00", "demanda": "5.699,00", "deficit": "-5.699,00"}}
            ]
        }},
        "alcantarillado": {{
            "bien_servicio": "Apoyo financiero para los usuarios de servicios públicos domiciliarios de alcantarillado en los estratos 1 y 2.",
            "medido": "Número",
            "descripcion": "Entrega de subsidios destinados a satisfacer necesidades básicas para los usuarios de servicios públicos de alcantarillado en los estratos 1 y 2.",
            "descripcion_demanda": "Corresponde a la cantidad de subsidios que se requiere otorgar para satisfacer necesidades básicas para los usuarios de servicios públicos domiciliarios de alcantarillado en los estratos 1 y 2.",
            "descripcion_oferta": "Corresponde a la cantidad de subsidios que se otorgan.",
            "tabla_oferta_demanda": [
                {{"ano": "2021", "oferta": "2.725,00", "demanda": "2.725,00", "deficit": "0,00"}},
                {{"ano": "2022", "oferta": "2.748,00", "demanda": "2.748,00", "deficit": "0,00"}},
                {{"ano": "2023", "oferta": "2.771,00", "demanda": "2.771,00", "deficit": "0,00"}},
                {{"ano": "2024", "oferta": "2.775,00", "demanda": "2.775,00", "deficit": "0,00"}},
                {{"ano": "2025", "oferta": "3.044,00", "demanda": "3.044,00", "deficit": "0,00"}},
                {{"ano": "2026", "oferta": "0,00", "demanda": "3.044,00", "deficit": "-3.044,00"}},
                {{"ano": "2027", "oferta": "0,00", "demanda": "3.044,00", "deficit": "-3.044,00"}}
            ]
        }},
        "acueducto": {{
            "bien_servicio": "Apoyo financiero para los usuarios de servicios públicos domiciliarios de acueducto en los estratos 1 y 2.",
            "medido": "Número",
            "descripcion": "Entrega de subsidios destinados a satisfacer necesidades básicas para los usuarios de servicios públicos de acueducto en los estratos 1 y 2.",
            "descripcion_demanda": "Corresponde a la cantidad de subsidios que se requiere otorgar para satisfacer necesidades básicas para los usuarios de servicios públicos domiciliarios de acueducto en los estratos 1 y 2.",
            "descripcion_oferta": "Corresponde a la cantidad de subsidios que se otorgan.",
            "tabla_oferta_demanda": [
                {{"ano": "2021", "oferta": "5.440,00", "demanda": "5.440,00", "deficit": "0,00"}},
                {{"ano": "2022", "oferta": "5.513,00", "demanda": "5.513,00", "deficit": "0,00"}},
                {{"ano": "2023", "oferta": "5.586,00", "demanda": "5.586,00", "deficit": "0,00"}},
                {{"ano": "2024", "oferta": "5.588,00", "demanda": "5.588,00", "deficit": "0,00"}},
                {{"ano": "2025", "oferta": "5.748,00", "demanda": "5.748,00", "deficit": "0,00"}},
                {{"ano": "2026", "oferta": "0,00", "demanda": "5.748,00", "deficit": "-5.748,00"}},
                {{"ano": "2027", "oferta": "0,00", "demanda": "5.748,00", "deficit": "-5.748,00"}}
            ]
        }}
    }}
}}
"""

PROMPT_MGA_SUBSIDIOS_PAGINAS_12_16 = """
Genera contenido para las PÁGINAS 12-16 del documento MGA Subsidios.

DATOS DEL PROYECTO:
Municipio: {municipio} | Departamento: {departamento}
Proyecto: "{nombre_proyecto}"
Valor Total: ${valor_total} COP

RESPONDE CON JSON VÁLIDO:

{{
    "pagina_12_analisis_tecnico": {{
        "descripcion_alternativa": "La alternativa seleccionada consiste en la asignación de subsidios a las tarifas de los servicios públicos domiciliarios de Acueducto, Alcantarillado y Aseo, con el fin de garantizar el acceso equitativo y sostenible a dichos servicios por parte de los hogares de estratos 1 y 2 del municipio de {municipio}, {departamento}, en cumplimiento de los principios de solidaridad y redistribución del ingreso, consagrados en la Constitución Política y en la Ley 142 de 1994.",
        "descripcion_subsidios": "Los subsidios se otorgarán a los usuarios suscritos con menor capacidad económica, de acuerdo con la estratificación socioeconómica vigente, y serán aplicados directamente sobre las tarifas plenas del servicio, según los porcentajes definidos por la normativa y los acuerdos municipales.",
        "datos_linea_base": {{
            "fecha_corte": "diciembre de 2025",
            "acueducto": {{
                "estrato_1": {{"usuarios": "5.101", "tarifa_plena": "$9.724,70", "subsidio": "50%"}},
                "estrato_2": {{"usuarios": "647", "tarifa_plena": "$9.724,70", "subsidio": "30%"}}
            }},
            "alcantarillado": {{
                "estrato_1": {{"usuarios": "2.444", "tarifa_plena": "$5.318,37", "subsidio": "50%"}},
                "estrato_2": {{"usuarios": "600", "tarifa_plena": "$5.318,37", "subsidio": "30%"}}
            }},
            "aseo": {{
                "estrato_1": {{"usuarios": "5.047", "tarifa_plena": "$22.451,97", "subsidio": "50%"}},
                "estrato_2": {{"usuarios": "652", "tarifa_plena": "$22.935,88", "subsidio": "30%"}}
            }}
        }},
        "implementacion": "La implementación se realizará mediante convenio interadministrativo con EMACALA S.A.S E.S.P, quien aplicará los subsidios directamente en la facturación, de acuerdo con las condiciones pactadas en el acto administrativo o contrato. Los recursos serán contabilizados en cuentas especiales dentro del municipio, en cumplimiento de lo establecido en el Fondo de Solidaridad y Redistribución del Ingreso (FSRI).",
        "beneficio": "Esta alternativa permitirá beneficiar a una población proyectada de aproximadamente 5.681 hogares anuales en el periodo 2026, con el propósito de reducir el déficit identificado, mejorar la equidad tarifaria y contribuir al cumplimiento del Plan de Desarrollo Municipal."
    }},

    "pagina_13_localizacion": {{
        "ubicacion": {{
            "region": "Caribe",
            "departamento": "{departamento}",
            "municipio": "{municipio}",
            "tipo_agrupacion": "",
            "agrupacion": "",
            "latitud": "",
            "longitud": ""
        }},
        "factores_analizados": [
            "Aspectos administrativos y políticos",
            "Disponibilidad de servicios públicos domiciliarios (Agua, energía y otros)",
            "Factores ambientales",
            "Otros"
        ]
    }},

    "pagina_14_cadena_valor": {{
        "costo_total": "{valor_total}",
        "objetivo_especifico": {{
            "numero": "1",
            "descripcion": "Identificar y focalizar adecuadamente la población usuaria de los estratos 1 y 2 con derecho a subsidio en los servicios públicos domiciliarios.",
            "costo": "{valor_total}"
        }},
        "producto": {{
            "codigo": "1.1",
            "nombre": "Servicio de apoyo financiero para subsidios al consumo en los servicios públicos domiciliarios",
            "complemento": "(Producto principal del proyecto)",
            "medido": "Número de usuarios",
            "cantidad": "5.748,0000",
            "costo": "{valor_total}",
            "etapa": "Inversión",
            "localizacion": "{municipio}",
            "num_personas": "30104",
            "acumulativo": "No Acumulativo",
            "poblacion_beneficiaria": "30104"
        }},
        "actividades": [
            {{
                "codigo": "1.1.1",
                "descripcion": "Realizar el pago de los aportes para subsidiar a los usuarios de los servicios públicos domiciliarios de Acueducto de los estratos uno (1) y dos (2) del municipio de {municipio}, {departamento}.",
                "costo": "768.997.092,00",
                "etapa": "Inversión"
            }},
            {{
                "codigo": "1.1.2",
                "descripcion": "Realizar el pago de los aportes para subsidiar a los usuarios de los servicios públicos domiciliarios de Alcantarillado de los estratos uno (1) y dos (2) del municipio de {municipio}, {departamento}.",
                "costo": "217.088.132,00",
                "etapa": "Inversión"
            }},
            {{
                "codigo": "1.1.3",
                "descripcion": "Realizar el pago de los aportes para subsidiar a los usuarios de los servicios públicos domiciliarios de Aseo de los estratos uno (1) y dos (2) del municipio de {municipio}, {departamento}.",
                "costo": "676.479.852,00",
                "etapa": "Inversión"
            }}
        ]
    }},

    "pagina_15_actividades_detalle": {{
        "actividades_periodo": [
            {{
                "codigo": "1.1.1",
                "nombre": "Acueducto",
                "periodos": [{{"periodo": "1", "valor": "$768.997.092,00"}}],
                "total": "$768.997.092,00"
            }},
            {{
                "codigo": "1.1.2",
                "nombre": "Alcantarillado",
                "periodos": [{{"periodo": "1", "valor": "$217.088.132,00"}}],
                "total": "$217.088.132,00"
            }},
            {{
                "codigo": "1.1.3",
                "nombre": "Aseo",
                "periodos": [{{"periodo": "1", "valor": "$676.479.852,00"}}],
                "total": "$676.479.852,00"
            }}
        ]
    }},

    "pagina_16_riesgos": {{
        "riesgos": [
            {{
                "nivel": "1-Propósito (Objetivo general)",
                "tipo": "Administrativos",
                "descripcion": "Demora en el trámite del acuerdo municipal de tarifas",
                "probabilidad": "4. Probable",
                "impacto": "4. Mayor",
                "efectos": "Incremento en el cobro del servicio por cada suscriptor",
                "mitigacion": "Realizar los trámites administrativos pertinentes y en los tiempos establecidos para la aprobación de tarifas y Acuerdo municipal."
            }},
            {{
                "nivel": "2-Componente (Productos)",
                "tipo": "Operacionales",
                "descripcion": "Error en el cálculo de subsidios de acueducto, alcantarillado y aseo otorgados a los usuarios de estratos 1 y 2",
                "probabilidad": "1. Raro",
                "impacto": "4. Mayor",
                "efectos": "Cobro excesivo en las tarifas",
                "mitigacion": "Supervisión directa de la secretaría de Planeación en la verificación de los cálculos de los subsidios asignados."
            }},
            {{
                "nivel": "3-Actividad y/o Entregable",
                "tipo": "Financieros",
                "descripcion": "Actividad/Entregable: 1.1.1 Realizar el pago de los aportes para subsidiar a los usuarios de los servicios públicos domiciliarios de Acueducto de los estratos uno (1) y dos (2) del municipio de {municipio}, {departamento}.",
                "probabilidad": "1. Raro",
                "impacto": "5. Catastrófico",
                "efectos": "Incremento en el pago de los servicios, inconformismo por el no pago de los subsidios, Protestas y manifestaciones en contra de la administración municipal.",
                "mitigacion": "Gestión financiera de los recursos"
            }}
        ]
    }}
}}
"""

PROMPT_MGA_SUBSIDIOS_PAGINAS_17_21 = """
Genera contenido para las PÁGINAS 17-21 del documento MGA Subsidios.

DATOS DEL PROYECTO:
Municipio: {municipio} | Departamento: {departamento}
Proyecto: "{nombre_proyecto}"
Valor Total: ${valor_total} COP

RESPONDE CON JSON VÁLIDO:

{{
    "pagina_17_riesgos_continuacion": {{
        "riesgos_adicionales": [
            {{
                "nivel": "3-Actividad y/o Entregable",
                "tipo": "Financieros",
                "descripcion_actividad": "Actividad/Entregable: 1.1.2 Realizar el pago de los aportes para subsidiar a los usuarios de los servicios públicos domiciliarios de Alcantarillado de los estratos uno (1) y dos (2) del municipio de {municipio}, {departamento}.",
                "descripcion_riesgo": "Riesgo: Insuficientes recursos para otorgar subsidios de Alcantarillado durante toda la vigencia.",
                "probabilidad": "1. Raro",
                "impacto": "5. Catastrófico",
                "efectos": "subsidios, Protestas y manifestaciones en contra de la administración municipal",
                "mitigacion": "Gestión financiera de los recursos"
            }},
            {{
                "nivel": "3-Actividad y/o Entregable",
                "tipo": "Financieros",
                "descripcion_actividad": "Actividad/Entregable: 1.1.3 Realizar el pago de los aportes para subsidiar a los usuarios de los servicios públicos domiciliarios de Aseo de los estratos uno (1) y dos (2) del municipio de {municipio}, {departamento}.",
                "descripcion_riesgo": "Riesgo: Insuficientes recursos para otorgar subsidios de Aseo durante toda la vigencia.",
                "probabilidad": "1. Raro",
                "impacto": "5. Catastrófico",
                "efectos": "Incremento en el pago de los servicios, Inconformismo por el no pago de los subsidios, Protestas y manifestaciones en contra de la administración municipal.",
                "mitigacion": "Gestión financiera de los recursos"
            }}
        ]
    }},

    "pagina_18_19_ingresos_beneficios": {{
        "descripcion": "Ahorro monetario anual en el pago total de las facturas de los servicios públicos domiciliarios de Aseo, Alcantarillado y Acueducto",
        "tipo": "Beneficios",
        "medido": "Número",
        "bien_producido": "Otros",
        "razon_precio_cuenta": "0.80",
        "descripcion_cantidad": "Corresponde al total de usuarios que reciben subsidios de servicios públicos de Acueducto, Alcantarillado y Aseo.",
        "descripcion_valor_unitario": "Corresponde al valor promedio de ahorro en el pago de los servicios públicos domiciliarios de Acueducto, Alcantarillado y Aseo.",
        "tabla_periodos": [
            {{"periodo": "1", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "2", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "3", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "4", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "5", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "6", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "7", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "8", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "9", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "10", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "11", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}},
            {{"periodo": "12", "cantidad": "5.748,00", "valor_unitario": "$24.102,37", "valor_total": "$138.540.422,76"}}
        ],
        "tabla_totales": [
            {{"periodo": "1", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "2", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "3", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "4", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "5", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "6", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "7", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "8", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "9", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "10", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "11", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}},
            {{"periodo": "12", "total_beneficios": "$138.540.422,76", "total": "$138.540.422,76"}}
        ]
    }},

    "pagina_20_flujo_economico": {{
        "alternativa": "Alternativa 1",
        "flujo": [
            {{"p": "0", "beneficios": "$0,0", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$0,0"}},
            {{"p": "1", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$2.443.970.661,7", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$-2.333.138.323,5"}},
            {{"p": "2", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}},
            {{"p": "3", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}},
            {{"p": "4", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}},
            {{"p": "5", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}},
            {{"p": "6", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}},
            {{"p": "7", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}},
            {{"p": "8", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}},
            {{"p": "9", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}},
            {{"p": "10", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}},
            {{"p": "11", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}},
            {{"p": "12", "beneficios": "$110.832.338,2", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "salvamento": "$0,0", "flujo_neto": "$110.832.338,2"}}
        ]
    }},

    "pagina_21_indicadores_decision": {{
        "evaluacion_economica": {{
            "vpn": "$-1.448.534.993,32",
            "tir": "-9,51 %",
            "rcb": "$0,35",
            "costo_beneficiario": "$74.480,96",
            "valor_presente_costos": "$2.242.174.919,01",
            "cae": "$-193.475.835,69"
        }},
        "costo_capacidad": {{
            "producto": "Servicio de apoyo financiero para subsidios al consumo en los servicios públicos domiciliarios (Producto principal del proyecto)",
            "costo_unitario": "$390.079,14"
        }},
        "decision": {{
            "alternativa": "Transferir los recursos de subsidios para los servicios públicos domiciliarios de Acueducto, Alcantarillado y Aseo a la EMACALA S.A.S E.S.P"
        }},
        "alcance": "Identificar y focalizar adecuadamente la población usuaria de los estratos 1 y 2 con derecho a subsidio en los servicios públicos domiciliarios. Servicio de apoyo financiero para subsidios al consumo en los servicios públicos domiciliarios (Producto principal del proyecto). Medido a través de: Número de usuarios. Cantidad: 5.748 con el fin de: Mejorar el acceso equitativo a los servicios públicos domiciliarios de acueducto, alcantarillado y aseo mediante el otorgamiento de subsidios a la población vulnerable de los estratos 1 y 2 del municipio de {municipio}. Familias subsidiadas en cobertura de Acueducto, Número: 6.332 {departamento}, {municipio}"
    }}
}}
"""

PROMPT_MGA_SUBSIDIOS_PAGINAS_22_24 = """
Genera contenido para las PÁGINAS 22-24 del documento MGA Subsidios.

DATOS DEL PROYECTO:
Municipio: {municipio} | Departamento: {departamento}
Proyecto: "{nombre_proyecto}"
Valor Total: ${valor_total} COP

RESPONDE CON JSON VÁLIDO:

{{
    "pagina_22_indicadores_producto": {{
        "objetivo": {{
            "numero": "1",
            "descripcion": "Identificar y focalizar adecuadamente la población usuaria de los estratos 1 y 2 con derecho a subsidio en los servicios públicos domiciliarios."
        }},
        "producto": {{
            "codigo": "1.1",
            "nombre": "Servicio de apoyo financiero para subsidios al consumo en los servicios públicos domiciliarios",
            "complemento": "(Producto principal del proyecto)"
        }},
        "indicador": {{
            "codigo": "1.1.1",
            "nombre": "Usuarios beneficiados con subsidios al consumo",
            "medido": "Número de usuarios",
            "meta_total": "5.748,0000",
            "formula": "",
            "es_acumulativo": "No",
            "es_principal": "Sí",
            "tipo_fuente": "Informe",
            "fuente_verificacion": "EMACALA S.A.S E.S.P y Secretaría de Planeación"
        }},
        "programacion_indicadores": [
            {{"periodo": "1", "meta": "$748,0000"}}
        ]
    }},

    "pagina_23_regionalizacion": {{
        "producto": "Servicio de apoyo financiero para subsidios al consumo en los servicios públicos domiciliarios (Producto principal del proyecto)",
        "ubicacion": {{
            "region": "Caribe",
            "departamento": "{departamento}",
            "municipio": "{municipio}",
            "tipo_agrupacion": "",
            "agrupacion": ""
        }},
        "tabla_costos": [
            {{
                "periodo": "1",
                "costo_total": "1.662.565.076,00",
                "costo_regionalizado": "1.662.565.076,00",
                "meta_total": "5748,0000",
                "meta_regionalizada": "5748,0000",
                "beneficiarios": "0"
            }}
        ]
    }},

    "pagina_24_focalizacion": {{
        "tabla_focalizacion": []
    }}
}}
"""
