"""
DTS (Documento Técnico de Soporte) Document Generator
Generates MGA-compliant Technical Support Documents with Word output
"""

import os
import sys
import json
import re
sys.path.append('..')

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from prompts.dts_structured import (
    DTS_SYSTEM_STRUCTURED,
    PROMPT_DTS_ESTRUCTURADO
)
from generators.dts_builder import DTSBuilder


class DTSGenerator:
    """Generator for DTS (Documento Técnico de Soporte) documents"""
    
    def __init__(self, llm, output_dir: str = "output"):
        """
        Initialize the generator with an LLM instance
        
        Args:
            llm: LangChain LLM instance
            output_dir: Directory for output files
        """
        self.llm = llm
        self.output_parser = StrOutputParser()
        self.builder = DTSBuilder(output_dir)
    
    def _create_chain(self, prompt_template: str, system_template: str = DTS_SYSTEM_STRUCTURED):
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
        
        return {}
    
    def generate_complete(self, data: dict) -> dict:
        """
        Generate the complete DTS document
        
        Args:
            data: Dictionary with all project information
            
        Returns:
            Dictionary with filepath and metadata
        """
        chain = self._create_chain(PROMPT_DTS_ESTRUCTURADO)
        
        response = chain.invoke({
            "municipio": data.get("municipio", ""),
            "departamento": data.get("departamento", ""),
            "entidad": data.get("entidad", ""),
            "bpin": data.get("bpin", ""),
            "nombre_proyecto": data.get("nombre_proyecto", ""),
            "objeto": data.get("objeto", ""),
            "valor_total": data.get("valor_total", ""),
            "duracion": data.get("duracion", "365"),
            "responsable": data.get("responsable", ""),
            "cargo": data.get("cargo", "Secretario de Planeación Municipal"),
            "programa": data.get("programa", ""),
            "subprograma": data.get("subprograma", ""),
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
                "tipo": "dts",
                "municipio": data.get("municipio", ""),
                "bpin": data.get("bpin", "")
            }
        }
