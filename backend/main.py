# backend/main.py
from fastapi import FastAPI
from .database import engine, Base
from . import survey

app = FastAPI(title="Basit Anket API")

# tabloları oluştur
Base.metadata.create_all(bind=engine)

# router ekle
app.include_router(survey.router)
