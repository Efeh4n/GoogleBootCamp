# backend/models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class SurveyResponse(Base):
    __tablename__ = "survey_responses"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False, index=True)

    # 77 sütun (q1‒q77). Hepsi 1‑5 arası puan tutacak
    q1  = Column(Integer);  q2  = Column(Integer);  q3  = Column(Integer)
    q4  = Column(Integer);  q5  = Column(Integer);  q6  = Column(Integer)
    q7  = Column(Integer);  q8  = Column(Integer);  q9  = Column(Integer)
    q10 = Column(Integer);  q11 = Column(Integer);  q12 = Column(Integer)
    q13 = Column(Integer);  q14 = Column(Integer);  q15 = Column(Integer)
    q16 = Column(Integer);  q17 = Column(Integer);  q18 = Column(Integer)
    q19 = Column(Integer);  q20 = Column(Integer);  q21 = Column(Integer)
    q22 = Column(Integer);  q23 = Column(Integer);  q24 = Column(Integer)
    q25 = Column(Integer);  q26 = Column(Integer);  q27 = Column(Integer)
    q28 = Column(Integer);  q29 = Column(Integer);  q30 = Column(Integer)
    q31 = Column(Integer);  q32 = Column(Integer);  q33 = Column(Integer)
    q34 = Column(Integer);  q35 = Column(Integer);  q36 = Column(Integer)
    q37 = Column(Integer);  q38 = Column(Integer);  q39 = Column(Integer)
    q40 = Column(Integer);  q41 = Column(Integer);  q42 = Column(Integer)
    q43 = Column(Integer);  q44 = Column(Integer);  q45 = Column(Integer)
    q46 = Column(Integer);  q47 = Column(Integer);  q48 = Column(Integer)
    q49 = Column(Integer);  q50 = Column(Integer);  q51 = Column(Integer)
    q52 = Column(Integer);  q53 = Column(Integer);  q54 = Column(Integer)
    q55 = Column(Integer);  q56 = Column(Integer);  q57 = Column(Integer)
    q58 = Column(Integer);  q59 = Column(Integer);  q60 = Column(Integer)
    q61 = Column(Integer);  q62 = Column(Integer);  q63 = Column(Integer)
    q64 = Column(Integer);  q65 = Column(Integer);  q66 = Column(Integer)
    q67 = Column(Integer);  q68 = Column(Integer);  q69 = Column(Integer)
    q70 = Column(Integer);  q71 = Column(Integer);  q72 = Column(Integer)
    q73 = Column(Integer);  q74 = Column(Integer);  q75 = Column(Integer)
    q76 = Column(Integer);  q77 = Column(Integer)
