from app.pdf_parser import parse_pdf

def test_parse_pdf():
    class MockFile:
        def read(self):
            return b'%PDF-1.4 mock pdf content'
    
    parsed_text = parse_pdf(MockFile())
    assert isinstance(parsed_text, str)