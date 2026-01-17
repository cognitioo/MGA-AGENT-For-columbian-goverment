"""
Unified MGA Document Generator
Orchestrates the generation of all supporting documents in parallel.
"""

import os
import zipfile
import concurrent.futures
from datetime import datetime
from typing import Dict, List, Any

# Import individual generators
from generators.estudios_previos_generator import EstudiosPreviosGenerator
from generators.analisis_sector_generator import AnalisisSectorGenerator
from generators.dts_generator import DTSGenerator
from generators.certificaciones_generator import CertificacionesGenerator
from generators.mga_subsidios_generator import MGASubsidiosGenerator
from config import get_llm

class UnifiedGenerator:
    """
    Orchestrates the generation of all MGA supporting documents.
    """
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate_all(self, data: Dict[str, Any], model_name: str = "groq") -> Dict[str, Any]:
        """
        Generate all documents in parallel.
        
        Args:
            data: Unified data dictionary containing all project info.
            model_name: Name of the LLM model to use.
            
        Returns:
            Dictionary with results...
        """
        # Initialize LLM
        try:
            llm = get_llm(model_name)
        except Exception as e:
            return {"success": False, "results": [], "error": f"LLM init failed: {e}"}
            
        # Initialize generators with LLM
        generators = {
            "estudios_previos": EstudiosPreviosGenerator(llm),
            "analisis_sector": AnalisisSectorGenerator(llm),
            "dts": DTSGenerator(llm),
            "certificaciones": CertificacionesGenerator(llm),
            "mga_subsidios": MGASubsidiosGenerator(llm)
        }

        results = []
        files_to_zip = []
        
        # Define tasks
        tasks = {
            "estudios_previos": generators["estudios_previos"].generate_complete,
            "analisis_sector": generators["analisis_sector"].generate_complete,
            "dts": generators["dts"].generate_complete,
            "certificaciones": generators["certificaciones"].generate_complete,
            "mga_subsidios": generators["mga_subsidios"].generate_complete
        }
        
        # Execute in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_type = {
                executor.submit(func, data): doc_type 
                for doc_type, func in tasks.items()
            }
            
            for future in concurrent.futures.as_completed(future_to_type):
                doc_type = future_to_type[future]
                try:
                    # Note: Most generators return a dict with 'filepath' or similar
                    # We might need to adjust based on exact return signature of each generator
                    # EstudiosPrevios: returns filepath (str) or dict? Let's assume consistent interface or handle variance
                    result = future.result()
                    
                    # Handle different return types
                    filepath = None
                    if isinstance(result, str):
                        filepath = result
                    elif isinstance(result, dict) and "filepath" in result:
                        filepath = result["filepath"]
                    
                    if filepath and os.path.exists(filepath):
                        results.append({
                            "type": doc_type,
                            "status": "success",
                            "file": filepath
                        })
                        files_to_zip.append(filepath)
                    else:
                        results.append({
                            "type": doc_type,
                            "status": "error",
                            "error": "File not created or invalid return type"
                        })
                        
                except Exception as e:
                    results.append({
                        "type": doc_type,
                        "status": "error",
                        "error": str(e)
                    })
                    print(f"Error generating {doc_type}: {e}")

        # Create ZIP if we have files
        zip_path = None
        if files_to_zip:
            zip_path = self._create_zip(files_to_zip, data.get("municipio", "proyecto"))
            
        return {
            "success": len(files_to_zip) > 0,
            "results": results,
            "zip_file": zip_path
        }
    
    def _create_zip(self, file_paths: List[str], project_name: str) -> str:
        """Create a ZIP archive of the generated files."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = "".join(x for x in project_name if x.isalnum() or x in (' ', '-', '_')).strip()
        zip_filename = f"MGA_Documentos_{safe_name}_{timestamp}.zip"
        zip_filepath = os.path.join(self.output_dir, zip_filename)
        
        with zipfile.ZipFile(zip_filepath, 'w') as zipf:
            for file in file_paths:
                zipf.write(file, os.path.basename(file))
                
        return zip_filepath
