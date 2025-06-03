# utils/parser.py

import PyPDF2

def extract_text_from_pdf(file):
    """
    Extracts full text from all pages of a PDF file.
    """
    reader = PyPDF2.PdfReader(file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
    return full_text.strip()
