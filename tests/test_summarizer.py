from app.utils import *
from app.summarizer import generate_summary
import pytest

def test_generate_summary():
    sample_text = "This is a test document. It contains important information."
    summary = generate_summary(
        sample_text,
        summary_type="Brief",
        model="gpt-3.5-turbo",
        max_tokens=300,
        temperature=0.5
    )
    assert isinstance(summary, str)
    assert len(summary) > 0
