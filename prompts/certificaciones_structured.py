"""
Presentación y Certificaciones (Presentation & Certificates) Structured Prompt Templates
MGA support documents for project certification
"""

from .base_prompts import MGA_CONTEXT

CERTIFICACIONES_SYSTEM = f"""
{MGA_CONTEXT}

Tu tarea es generar contenido para documentos de PRESENTACIÓN y CERTIFICACIONES de proyectos MGA.

**DOCUMENTOS A GENERAR:**
1. Carta de Presentación del Proyecto (al Alcalde)
2. Certificación de inclusión en Plan de Desarrollo
3. Certificación de Precios Unitarios
4. Certificación de No Financiación con otras fuentes
5. Certificación de Sostenibilidad
6. Certificación de Viabilidad Institucional
7. Certificación de Localización (no riesgo)
8. Certificación de Normas Técnicas NTC

**REGLAS:**
• Responde SOLO en JSON válido
• Usa lenguaje formal y oficial
• Incluye fechas y datos específicos
• Mantén el formato de certificación oficial colombiana
"""

PROMPT_CERTIFICACIONES = """
Genera contenido para documentos de PRESENTACIÓN y CERTIFICACIONES MGA.

DATOS DEL PROYECTO:
Municipio: {municipio} | Departamento: {departamento}
Entidad: {entidad} | BPIN: {bpin}
Proyecto: "{nombre_proyecto}"
Valor: ${valor_total} COP
Responsable: {responsable} ({cargo})
Fecha: {fecha}
Alcalde: {alcalde}
Plan de Desarrollo: {plan_desarrollo}

CONTEXTO ADICIONAL DEL DOCUMENTO (DUMP DATA):
{context_dump}

RESPONDE CON JSON VÁLIDO:

{{
    "carta_presentacion": {{
        "destinatario": "Doctor\\n{alcalde}\\nAlcalde Municipal",
        "referencia": "Presentación Proyecto",
        "cuerpo": "De manera atenta hago entrega a usted el proyecto \\"{nombre_proyecto}\\" ajustado de acuerdo con la metodología recomendada por el DNP y elaborado dentro de la Metodología General Ajustada (MGA), para su respectiva evaluación, viabilización y aprobación, con el objetivo de solicitar ${valor_total} para la ejecución dentro de los siguientes lineamientos:\\n\\n• El proyecto se encuentra incluido dentro del Plan de Gobierno.\\n• El costo total del Proyecto es de: ${valor_total}\\n• El valor que aportará el municipio de {municipio}: ${valor_total}\\n\\nCumpliendo con los requisitos exigidos por la METODOLOGÍA GENERAL AJUSTADA, anexo esta solicitud los siguientes documentos:\\n\\n✓ CARTA REMISORA DEL PROYECTO AL BANCO DE PROGRAMAS Y PROYECTOS MUNICIPAL\\n✓ CARTA DE PRESENTACIÓN DEL PROYECTO\\n✓ METODOLOGÍA GENERAL AJUSTADA MGA (Impresos los formatos que validan la metodología)\\n✓ MEDIO MAGNÉTICO (Incluye cronograma, metodología, presupuesto y ordenanzas)\\n✓ LOCALIZACIÓN GENERAL (MACRO) Y UBICACIÓN ESPECÍFICA (MICRO) - MAPA\\n✓ PRESUPUESTO ACTUALIZADO",
        "despedida": "Agradeciendo su atención,"
    }},

    "cert_plan_desarrollo": {{
        "titulo": "EL SECRETARIO DE PLANEACIÓN DEL MUNICIPIO DE {municipio}\\nDEPARTAMENTO DE {departamento}",
        "encabezado": "CERTIFICA",
        "contenido": "Que el proyecto de inversión denominado \\"{nombre_proyecto}\\" está incluido entre los programas y proyectos del Plan de Desarrollo {plan_desarrollo}.",
        "fecha_expedicion": "Dado en el municipio de {municipio} departamento de {departamento}, a los {dia} días del mes de {mes} de {ano}"
    }},

    "cert_precios_unitarios": {{
        "titulo": "EL SECRETARIO DE PLANEACIÓN DEL MUNICIPIO DE {municipio}\\nDEPARTAMENTO DE {departamento}",
        "encabezado": "CERTIFICA",
        "contenido": "Que los precios unitarios corresponden al promedio de la región y que son los utilizados para el tipo de actividades contempladas en el proyecto de inversión \\"{nombre_proyecto}\\"",
        "fecha_expedicion": "La presente certificación se expide a los {dia} días del mes de {mes} de {ano}"
    }},

    "cert_no_financiacion": {{
        "titulo": "EL SECRETARIO DE PLANEACIÓN DEL MUNICIPIO DE {municipio}\\nDEPARTAMENTO DE {departamento}",
        "encabezado": "CERTIFICA",
        "contenido": "Que las actividades que se pretenden financiar del proyecto de inversión denominado \\"{nombre_proyecto}\\" no han sido financiadas con otras fuentes de recursos.",
        "fecha_expedicion": "La presente certificación se expide a los {dia} días del mes de {mes} de {ano}"
    }},

    "cert_sostenibilidad": {{
        "titulo": "EL SECRETARIO DE PLANEACIÓN DEL MUNICIPIO DE {municipio}\\nDEPARTAMENTO DE {departamento}",
        "encabezado": "CERTIFICA",
        "contenido": "Que de acuerdo con la naturaleza de los bienes y servicios a entregar contemplados en el proyecto de inversión denominado \\"{nombre_proyecto}\\", estos no generarán costos de sostenibilidad en su operación y funcionamiento.",
        "fecha_expedicion": "La presente certificación se expide a los {dia} días del mes de {mes} de {ano}"
    }},

    "cert_viabilidad": {{
        "titulo": "EL SECRETARIO DE PLANEACIÓN DEL MUNICIPIO DE {municipio}\\nDEPARTAMENTO DE {departamento}",
        "encabezado": "CERTIFICA",
        "contenido": "Que revisado el proyecto de inversión denominado \\"{nombre_proyecto}\\", lo encuentra acorde con los requisitos y lineamientos vigentes para la formulación de proyecto; que evaluó técnicamente el proyecto de forma integral, en los aspectos metodológicos, técnicos, legales, socioeconómicos y ambientales por lo que indica que cumple con las condiciones y requisitos para que se le otorgue Viabilidad Institucional Favorable.",
        "fecha_expedicion": "La presente certificación se expide a los {dia} días del mes de {mes} de {ano}"
    }},

    "cert_localizacion": {{
        "titulo": "EL SECRETARIO DE PLANEACIÓN DEL MUNICIPIO DE {municipio}\\nDEPARTAMENTO DE {departamento}",
        "encabezado": "CERTIFICA",
        "contenido": "Que el proyecto de inversión \\"{nombre_proyecto}\\", no se encuentra localizado en zona que presente alto riesgo no mitigable y que está acorde con el uso y tratamientos del suelo de conformidad con el respectivo Esquema de Ordenamiento Territorial (EOT).",
        "fecha_expedicion": "La presente certificación se expide a los {dia} días del mes de {mes} de {ano}"
    }},

    "cert_normas_tecnicas": {{
        "titulo": "EL SECRETARIO DE PLANEACIÓN DEL MUNICIPIO DE {municipio}\\nDEPARTAMENTO DE {departamento}",
        "encabezado": "CERTIFICA",
        "contenido": "Que las especificaciones técnicas del proyecto denominado \\"{nombre_proyecto}\\", cumplen con las Normas Técnicas Colombianas (NTC) aplicables, y no aplica las normas que establecen mecanismos de integración para las personas con movilidad reducida.",
        "fecha_expedicion": "La presente certificación se expide a los {dia} días del mes de {mes} de {ano}"
    }}
}}
"""
