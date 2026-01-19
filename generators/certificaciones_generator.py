"""
Certificaciones Document Generator
Generates Presentation Letter and Certificates for MGA projects
"""

import os
import sys
import json
import re
from datetime import datetime
sys.path.append('..')

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from prompts.certificaciones_structured import (
    CERTIFICACIONES_SYSTEM,
    PROMPT_CERTIFICACIONES
)
from generators.certificaciones_builder import CertificacionesBuilder


class CertificacionesGenerator:
    """Generator for Presentation and Certificates documents"""
    
    def __init__(self, llm, output_dir: str = "output"):
        self.llm = llm
        self.output_parser = StrOutputParser()
        self.builder = CertificacionesBuilder(output_dir)
    
    def _create_chain(self, prompt_template: str, system_template: str = CERTIFICACIONES_SYSTEM):
        """Create a LangChain chain for a specific prompt"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_template),
            ("human", prompt_template)
        ])
        return prompt | self.llm | self.output_parser
    
    def _extract_json(self, response: str) -> dict:
        """Extract JSON from AI response"""
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            pass
        
        json_patterns = [
            r'```json\s*([\s\S]*?)\s*```',
            r'```\s*([\s\S]*?)\s*```',
            r'\{[\s\S]*\}'
        ]
        
        for pattern in json_patterns:
            match = re.search(pattern, response)
            if match:
                try:
                    json_str = match.group(1) if '```' in pattern else match.group(0)
                    return json.loads(json_str)
                except (json.JSONDecodeError, IndexError):
                    continue
        
        return {}
    
    def _get_month_name(self, month: int) -> str:
        """Get Spanish month name"""
        months = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]
        return months[month - 1]
    
    def generate_complete(self, data: dict) -> dict:
        """
        Generate the complete Certificaciones document
        
        Args:
            data: Dictionary with all project information
            
        Returns:
            Dictionary with filepath and metadata
        """
        chain = self._create_chain(PROMPT_CERTIFICACIONES)
        
        now = datetime.now()
        
        response = chain.invoke({
            "municipio": data.get("municipio", ""),
            "departamento": data.get("departamento", ""),
            "entidad": data.get("entidad", ""),
            "bpin": data.get("bpin", ""),
            "nombre_proyecto": data.get("nombre_proyecto", ""),
            "valor_total": data.get("valor_total", ""),
            "responsable": data.get("responsable", ""),
            "cargo": data.get("cargo", "Secretario de Planeación Municipal"),
            "fecha": data.get("fecha", f"{now.day} de {self._get_month_name(now.month)} de {now.year}"),
            "alcalde": data.get("alcalde", ""),
            "plan_desarrollo": data.get("plan_desarrollo", ""),
            "dia": str(now.day),
            "mes": self._get_month_name(now.month),
            "ano": str(now.year),
            "context_dump": (data.get("context_dump", "No disponible") or "")[:3000]  # Truncate to avoid token limit
        })
        
        # Parse JSON from response
        ai_content = self._extract_json(response)
        
        # Build the Word document
        letterhead_file = data.get("letterhead_file")
        filepath = self.builder.build(data, ai_content, letterhead_file)
        
        return {
            "filepath": filepath,
            "documento_completo": response,
            "ai_content": ai_content,
            "metadata": {
                "tipo": "certificaciones",
                "municipio": data.get("municipio", ""),
                "bpin": data.get("bpin", "")
            }
        }
