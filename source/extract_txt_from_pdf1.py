import os
import sys
import glob
import fitz  # PyMuPDF library

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dir = sys.argv[1]
    else:
        print("Please provide a prefix")
        exit(1)

print(f'Extracting text from PDFs in {dir}/papers')

for pdf_file in glob.glob(f'{dir}/papers/*.pdf'):
    try:
        with fitz.open(pdf_file) as doc:
            text = ""
            for page in doc:
                text += page.get_text()

        base = os.path.splitext(pdf_file)[0]
        outfile = f'{base}.txt'
        print('Writing', outfile)

        with open(outfile, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Error processing {pdf_file}: {e}")