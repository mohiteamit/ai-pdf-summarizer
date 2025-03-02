import fitz  # PyMuPDF
import io

def parse_pdf(uploaded_file) -> str:
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()
