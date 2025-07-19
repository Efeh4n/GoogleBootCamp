# backend/schemas.py
from pydantic import BaseModel, Field

class StartRequest(BaseModel):
    full_name: str = Field(..., example="Efe Hazar")

class StartResponse(BaseModel):
    id: int
    message: str

class SurveyAnswer(BaseModel):
    respondent_id: int  # /start dönüşündeki id
    answer: int = Field(..., ge=1, le=5)

class Message(BaseModel):
    message: str
