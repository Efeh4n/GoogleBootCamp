# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:password@localhost:3306/anket_db")

engine = create_engine(DB_URL, echo=True)

# yoksa db’yi yarat
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
