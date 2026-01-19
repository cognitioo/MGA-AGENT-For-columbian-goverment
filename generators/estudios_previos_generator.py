"""
Estudios Previos (Prior Studies) Document Generator
Generates MGA-compliant Prior Studies documents using structured JSON output
"""

import sys
import json
import re
sys.path.append('..')

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from prompts.estudios_previos_structured import (
    ESTUDIOS_PREVIOS_SYSTEM_STRUCTURED,
    PROMPT_ESTUDIOS_PREVIOS_ESTRUCTURADO
)
from generators.estudios_previos_builder import EstudiosPreviosDirectBuilder


class EstudiosPreviosGenerator:
    """Generator for Estudios Previos (Prior Studies) documents"""
    
    def __init__(self, llm):
        """
        Initialize the generator with an LLM instance
        
        Args:
            llm: LangChain LLM instance (Gemini, OpenAI, Groq, or Anthropic)
        """
        self.llm = llm
        self.output_parser = StrOutputParser()
        self.builder = EstudiosPreviosDirectBuilder()
    
    def _create_chain(self, prompt_template: str):
        """Create a LangChain chain for a specific prompt"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", ESTUDIOS_PREVIOS_SYSTEM_STRUCTURED),
            ("human", prompt_template)
        ])
        return prompt | self.llm | self.output_parser
    
    def _extract_json(self, text: str) -> dict:
        """Extract JSON from AI response, handling markdown code blocks"""
        # Try to find JSON in code blocks first
        json_match = re.search(r'```(?:json)?\s*(\{[\s\S]*?\})\s*```', text)
        if json_match:
            text = json_match.group(1)
        
        # Try to find raw JSON object
        json_match = re.search(r'\{[\s\S]*\}', text)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                pass
        
        # Return empty structure if parsing fails
        return self._get_default_content()
    
    def _get_default_content(self) -> dict:
        """Get default content structure"""
        return {
            "marco_legal": "El Artículo 25 de la Ley 80 de 1993 establece los Estudios y Documentos Previos como requisito para la contratación.",
            "necesidad": "Se requiere la ejecución del proyecto para atender las necesidades identificadas en el municipio.",
            "objeto_alcance": "Realizar las actividades definidas en el convenio para cumplir con los objetivos del proyecto.",
            "especificaciones": [
                {"actividad": "Actividad 1", "descripcion": "Descripción de la actividad"},
                {"actividad": "Actividad 2", "descripcion": "Descripción de la actividad"},
            ],
            "obligaciones": {
                "municipio": "• Proveer los recursos financieros comprometidos.<br>• Facilitar el acceso a la información.",
                "empresa": "• Ejecutar las actividades técnicas descritas.<br>• Entregar los informes parciales y finales."
            },
            "fundamentos": "La contratación se enmarca en las disposiciones de la Ley 80 de 1993 y el Decreto 1082 de 2015.",
            "riesgos": [
                {"riesgo": "Retrasos en la ejecución", "probabilidad": "Media", "impacto": "Alto", "mitigacion": "Seguimiento periódico"},
            ],
            "presupuesto": [
                {"nombre": "Honorarios", "descripcion": "Costos de personal", "porcentaje": "60%", "valor": ""},
                {"nombre": "Operativos", "descripcion": "Gastos operacionales", "porcentaje": "40%", "valor": ""},
            ],
            "garantias": "Se exigirá garantía de cumplimiento equivalente al 10% del valor del contrato.",
            "plazo_lugar": "El plazo de ejecución será según lo establecido en el convenio.",
            "supervision": "La supervisión estará a cargo de un funcionario designado por la entidad contratante."
        }
    
    def _strip_section_titles(self, content: dict) -> dict:
        """Remove any section titles that the AI may have included in content"""
        # Patterns for section titles to remove
        patterns = [
            r'^\s*\d+\.\s*(MARCO\s+LEGAL|NECESIDAD|OBJETO|ALCANCE|OBLIGACIONES|FUNDAMENTOS|RIESGOS|PRESUPUESTO|GARANT[ÍI]AS|PLAZO|SUPERVISI[ÓO]N)[^\n]*\n?',
            r'^\s*NO\s+incluyas\s+el\s+t[ií]tulo[^\n]*\n?',
            r'^\s*CONTENIDO\s+LARGO[^\n]*\n?',
        ]
        
        for key, value in content.items():
            if isinstance(value, str):
                for pattern in patterns:
                    value = re.sub(pattern, '', value, flags=re.IGNORECASE | re.MULTILINE)
                content[key] = value.strip()
        
        return content
    
    def generate_complete(self, data: dict) -> dict:
        """
        Generate the complete Estudios Previos document
        
        Args:
            data: Dictionary with all project information
            
        Returns:
            Dictionary with filepath and metadata
        """
        chain = self._create_chain(PROMPT_ESTUDIOS_PREVIOS_ESTRUCTURADO)
        
        # Generate structured content
        response = chain.invoke({
            "municipio": data.get("municipio", ""),
            "departamento": data.get("departamento", ""),
            "entidad": data.get("entidad", ""),
            "tipo_proyecto": data.get("tipo_proyecto", ""),
            "bpin": data.get("bpin", ""),
            "necesidad": data.get("necesidad", ""),
            "objeto": data.get("objeto", ""),
            "alcance": data.get("alcance", ""),
            "valor_total": data.get("valor_total", ""),
            "fuente_financiacion": data.get("fuente_financiacion", ""),
            "rubros": data.get("rubros", ""),
            "plazo": data.get("plazo", "90"),
            "lugar": data.get("lugar", ""),
            "responsable": data.get("responsable", ""),
            "cargo": data.get("cargo", "Secretario de Planeación Municipal"),
            "context_dump": (data.get("context_dump", "No disponible") or "")[:3000]  # Truncate to avoid token limit
        })
        
        # Parse JSON from response
        ai_content = self._extract_json(response)
        
        # Post-process: strip any section titles the AI may have included
        ai_content = self._strip_section_titles(ai_content)
        
        # Merge form-provided obligaciones into AI content (user input takes priority)
        if data.get("obligaciones_municipio") or data.get("obligaciones_contratista"):
            ai_content["obligaciones"] = {
                "municipio": data.get("obligaciones_municipio", ai_content.get("obligaciones", {}).get("municipio", "")),
                "empresa": data.get("obligaciones_contratista", ai_content.get("obligaciones", {}).get("empresa", ""))
            }
        
        # Build the Word document directly
        letterhead_file = data.get("letterhead_file")
        filepath = self.builder.build(data, ai_content, letterhead_file)
        
        return {
            "filepath": filepath,
            "documento_completo": response,
            "ai_content": ai_content,
            "metadata": {
                "tipo": "estudios_previos",
                "municipio": data.get("municipio", ""),
                "bpin": data.get("bpin", "")
            }
        }
