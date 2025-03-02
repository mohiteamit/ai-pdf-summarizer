from fastapi import FastAPI, UploadFile, File
from app.summarizer import generate_summary
from app.pdf_parser import parse_pdf

app = FastAPI()

@app.post("/summarize")
async def summarize(file: UploadFile = File(...), summary_type: str = "Brief"):
    pdf_text = parse_pdf(file.file)
    if not pdf_text:
        return {"error": "Failed to extract text from PDF."}
    summary = await generate_summary(pdf_text, summary_type)
    return {"summary": summary}
