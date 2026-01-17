"""Fix the corrupted mga_subsidios_builder.py file"""

with open('generators/mga_subsidios_builder.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the first complete _save_document method and keep only that
# The good code ends at line ~1293 with "return docx_filepath"
# Everything after is duplicate/corrupted

# Split at the first "return docx_filepath" followed by the corrupted code
parts = content.split('            return docx_filepath')
if len(parts) >= 2:
    # Keep first part + one "return docx_filepath" + just a newline
    fixed_content = parts[0] + '            return docx_filepath\n'
else:
    fixed_content = content

with open('generators/mga_subsidios_builder.py', 'w', encoding='utf-8') as f:
    f.write(fixed_content)

print('File fixed - duplicate code removed')
