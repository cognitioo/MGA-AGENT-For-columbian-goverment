"""Update _save_document to output PDF"""
import re

new_save_document = '''    def _save_document(self, data):
        """Save the document to file as PDF"""
        from docx2pdf import convert
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        municipio = data.get("municipio", "documento")
        municipio = re.sub(r'[\\t\\n\\r\\\\\\\\/:\\"*?<>|]', '', municipio)
        municipio = municipio.replace(" ", "_").strip()
        if not municipio:
            municipio = "documento"
        
        # First save as DOCX
        docx_filename = f"MGA_Subsidios_{municipio}_{timestamp}.docx"
        docx_filepath = os.path.join(self.output_dir, docx_filename)
        self.doc.save(docx_filepath)
        
        # Convert to PDF
        pdf_filename = f"MGA_Subsidios_{municipio}_{timestamp}.pdf"
        pdf_filepath = os.path.join(self.output_dir, pdf_filename)
        
        try:
            convert(docx_filepath, pdf_filepath)
            # Remove temporary DOCX file
            os.remove(docx_filepath)
            return pdf_filepath
        except Exception as e:
            # If PDF conversion fails, return DOCX
            print(f"PDF conversion failed: {e}, returning DOCX")
            return docx_filepath'''

with open('generators/mga_subsidios_builder.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the _save_document method and replace it
pattern = r'    def _save_document\(self, data\):.*?return filepath'
new_content = re.sub(pattern, new_save_document, content, flags=re.DOTALL)

with open('generators/mga_subsidios_builder.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done - _save_document updated for PDF output')
