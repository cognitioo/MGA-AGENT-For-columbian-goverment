"""
MGA Subsidios Document Generator
Generates complete MGA documents for subsidies projects
"""

import os
import sys
import json
import re
import time
from datetime import datetime
sys.path.append('..')

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from prompts.mga_subsidios_structured import (
    MGA_SUBSIDIOS_SYSTEM,
    PROMPT_MGA_SUBSIDIOS_PAGINAS_1_5,
    PROMPT_MGA_SUBSIDIOS_PAGINAS_6_11,
    PROMPT_MGA_SUBSIDIOS_PAGINAS_12_16,
    PROMPT_MGA_SUBSIDIOS_PAGINAS_17_21,
    PROMPT_MGA_SUBSIDIOS_PAGINAS_22_24
)
from generators.mga_subsidios_builder import MGASubsidiosBuilder


class MGASubsidiosGenerator:
    """Generator for MGA Subsidios documents (24 pages)"""
    
    def __init__(self, llm, output_dir: str = "output"):
        self.llm = llm
        self.output_parser = StrOutputParser()
        self.builder = MGASubsidiosBuilder(output_dir)
    
    def _create_chain(self, prompt_template: str, system_template: str = MGA_SUBSIDIOS_SYSTEM):
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
    
    def generate_complete(self, data: dict) -> dict:
        """
        Generate the complete MGA Subsidios document (all 24 pages)
        
        Args:
            data: Dictionary with all project information
            
        Returns:
            Dictionary with filepath and metadata
        """
        now = datetime.now()
        
        invoke_data = {
            "municipio": data.get("municipio", ""),
            "departamento": data.get("departamento", ""),
            "entidad": data.get("entidad", ""),
            "bpin": data.get("bpin", ""),
            "nombre_proyecto": data.get("nombre_proyecto", ""),
            "valor_total": data.get("valor_total", ""),
            "duracion": data.get("duracion", "365"),
            "responsable": data.get("responsable", ""),
            "cargo": data.get("cargo", "Secretario de Planeación Municipal"),
            "identificador": data.get("identificador", ""),
            "fecha_creacion": data.get("fecha_creacion", now.strftime("%d/%m/%Y %H:%M:%S")),
            "plan_nacional": data.get("plan_nacional", "(2022-2026) Colombia Potencia Mundial de la Vida"),
            "plan_departamental": data.get("plan_departamental", "Bolívar Me Enamora 2024-2027"),
            "plan_municipal": data.get("plan_municipal", "San Pablo Mejor 2024-2027"),
            "context_dump": (data.get("context_dump", "No disponible") or "")[:3000]  # Truncate to avoid token limit
        }
        
        # Generate pages 1-5
        chain_1_5 = self._create_chain(PROMPT_MGA_SUBSIDIOS_PAGINAS_1_5)
        response_1_5 = chain_1_5.invoke(invoke_data)
        ai_content_1_5 = self._extract_json(response_1_5)
        print("MGA Page 1-5 done. Waiting 3s...")
        time.sleep(3) # Wait to avoid Rate Limit
        
        # Generate pages 6-11
        chain_6_11 = self._create_chain(PROMPT_MGA_SUBSIDIOS_PAGINAS_6_11)
        response_6_11 = chain_6_11.invoke(invoke_data)
        ai_content_6_11 = self._extract_json(response_6_11)
        print("MGA Page 6-11 done. Waiting 3s...")
        time.sleep(3) # Wait
        
        # Generate pages 12-16
        chain_12_16 = self._create_chain(PROMPT_MGA_SUBSIDIOS_PAGINAS_12_16)
        response_12_16 = chain_12_16.invoke(invoke_data)
        ai_content_12_16 = self._extract_json(response_12_16)
        print("MGA Page 12-16 done. Waiting 3s...")
        time.sleep(3) # Wait
        
        # Generate pages 17-21
        chain_17_21 = self._create_chain(PROMPT_MGA_SUBSIDIOS_PAGINAS_17_21)
        response_17_21 = chain_17_21.invoke(invoke_data)
        ai_content_17_21 = self._extract_json(response_17_21)
        print("MGA Page 17-21 done. Waiting 3s...")
        time.sleep(3) # Wait
        
        # Generate pages 22-24
        chain_22_24 = self._create_chain(PROMPT_MGA_SUBSIDIOS_PAGINAS_22_24)
        response_22_24 = chain_22_24.invoke(invoke_data)
        ai_content_22_24 = self._extract_json(response_22_24)
        
        # Merge all content
        ai_content = {**ai_content_1_5, **ai_content_6_11, **ai_content_12_16, **ai_content_17_21, **ai_content_22_24}
        
        # Build the Word document
        letterhead_file = data.get("letterhead_file")
        filepath = self.builder.build(data, ai_content, letterhead_file)
        
        return {
            "filepath": filepath,
            "documento_completo": response_1_5 + "\n\n" + response_6_11 + "\n\n" + response_12_16 + "\n\n" + response_17_21 + "\n\n" + response_22_24,
            "ai_content": ai_content,
            "metadata": {
                "tipo": "mga_subsidios",
                "municipio": data.get("municipio", ""),
                "bpin": data.get("bpin", ""),
                "paginas_generadas": "1-24"
            }
        }
