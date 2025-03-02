# tests/test_api.py
from app.utils import *
from fastapi.testclient import TestClient
from api.api import app
import os

client = TestClient(app)

def test_summarize_endpoint():
    pdf_path = "data/sample_pdfs/1. The Metamorphosis, Franz Kafka - Chapter 01.pdf"
    
    # Ensure the file exists before testing
    assert os.path.exists(pdf_path), f"File not found: {pdf_path}"
    
    with open(pdf_path, "rb") as pdf_file:
        response = client.post(
            "/summarize", 
            files={"file": ("test.pdf", pdf_file, "application/pdf")},
            data={"summary_type": "Brief"}
        )
        
    assert response.status_code == 200
    assert "summary" in response.json()
    assert len(response.json()["summary"]) > 0
