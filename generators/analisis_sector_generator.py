"""
Análisis del Sector (Sector Analysis) Document Generator
Generates MGA-compliant Sector Analysis documents with Word output
Uses structured prompts and dedicated document builder
"""

import os
import sys
import json
import re
sys.path.append('..')

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from prompts.analisis_sector_structured import (
    ANALISIS_SECTOR_SYSTEM_STRUCTURED,
    PROMPT_ANALISIS_SECTOR_ESTRUCTURADO
)
from generators.analisis_sector_builder import AnalisisSectorBuilder


class AnalisisSectorGenerator:
    """Generator for Análisis del Sector (Sector Analysis) documents"""
    
    def __init__(self, llm, output_dir: str = "output"):
        """
        Initialize the generator with an LLM instance
        
        Args:
            llm: LangChain LLM instance (Gemini, OpenAI, or Anthropic)
            output_dir: Directory for output files
        """
        self.llm = llm
        self.output_parser = StrOutputParser()
        self.builder = AnalisisSectorBuilder(output_dir)
    
    def _create_chain(self, prompt_template: str, system_template: str = ANALISIS_SECTOR_SYSTEM_STRUCTURED):
        """Create a LangChain chain for a specific prompt"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_template),
            ("human", prompt_template)
        ])
        return prompt | self.llm | self.output_parser
    
    def _extract_json(self, response: str) -> dict:
        """Extract JSON from AI response"""
        try:
            # Try direct JSON parse
            return json.loads(response)
        except json.JSONDecodeError:
            pass
        
        # Try to find JSON in code blocks
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
        
        # Return empty dict if extraction fails
        return {}
    
    def _strip_section_titles(self, content: dict) -> dict:
        """Remove section titles from AI-generated content"""
        title_patterns = [
            r'^1\.\s*OBJETO[:\s]*',
            r'^1\.1\s*DESCRIPCIÓN[:\s]*',
            r'^1\.4\s*ANÁLISIS[:\s]*',
            r'^\d+\.\d*\.?\s*[A-ZÁÉÍÓÚÑ\s]+[:\s]*',
        ]
        
        for key, value in content.items():
            if isinstance(value, str):
                for pattern in title_patterns:
                    value = re.sub(pattern, '', value, flags=re.IGNORECASE | re.MULTILINE)
                content[key] = value.strip()
        
        return content
    
    def generate_complete(self, data: dict) -> dict:
        """
        Generate the complete Análisis del Sector document
        
        Args:
            data: Dictionary with all project information
            
        Returns:
            Dictionary with filepath and metadata
        """
        chain = self._create_chain(PROMPT_ANALISIS_SECTOR_ESTRUCTURADO)
        
        response = chain.invoke({
            "numero_contrato": data.get("numero_contrato", ""),
            "modalidad": data.get("modalidad", "Convenio Interadministrativo"),
            "municipio": data.get("municipio", ""),
            "departamento": data.get("departamento", ""),
            "entidad": data.get("entidad", ""),
            "nombre_proyecto": data.get("nombre_proyecto", ""),
            "bpin": data.get("bpin", ""),
            "objeto": data.get("objeto", ""),
            "sector": data.get("sector", "Consultoría Ambiental"),
            "codigo_ciiu": data.get("codigo_ciiu", "7110"),
            "codigos_unspsc": data.get("codigos_unspsc", ""),
            "valor_total": data.get("valor_total", ""),
            "fuente": data.get("fuente_financiacion", ""),
            "duracion": data.get("duracion", "90"),
            "responsable": data.get("responsable", ""),
            "cargo": data.get("cargo", "Secretario de Planeación Municipal"),
            "context_dump": (data.get("context_dump", "No disponible") or "")[:3000]  # Truncate to avoid token limit
        })
        
        # Parse JSON from response
        ai_content = self._extract_json(response)
        
        # Post-process: strip section titles
        ai_content = self._strip_section_titles(ai_content)
        
        # Build the Word document
        letterhead_file = data.get("letterhead_file")
        section_toggles = data.get("section_toggles", {})
        filepath = self.builder.build(data, ai_content, letterhead_file, section_toggles)
        
        return {
            "filepath": filepath,
            "documento_completo": response,
            "ai_content": ai_content,
            "metadata": {
                "tipo": "analisis_sector",
                "municipio": data.get("municipio", ""),
                "bpin": data.get("bpin", "")
            }
        }
