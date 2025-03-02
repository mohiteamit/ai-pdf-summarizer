# api/models.py
from pydantic import BaseModel

class SummaryRequest(BaseModel):
    summary_type: str = "Brief"

class SummaryResponse(BaseModel):
    summary: str
