# backend/survey.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import SurveyResponse
from .schemas import StartRequest, StartResponse, SurveyAnswer, Message

router = APIRouter(prefix="/survey", tags=["Survey"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------- 1) Kullanıcı anketi başlatır
@router.post("/start", response_model=StartResponse)
def start_survey(data: StartRequest, db: Session = Depends(get_db)):
    resp = SurveyResponse(full_name=data.full_name)
    db.add(resp); db.commit(); db.refresh(resp)
    return {"id": resp.id, "message": f"{data.full_name} için anket başlatıldı."}

# ------- 2) Sorular sözlüğü
QUESTIONS = {
    1: "Sosyal ortamlarda enerji kazanırım.",
    2: "Gerçekçi düşünceler benim için daha değerlidir.",
    3: "Hayal dünyasında olmak, rutin işlerden daha kötüdür.",
    4: "İlkeler beni duygulardan daha çok etkiler.",
    5: "Mantıklı argümanlar duygusal olanlardan daha çok ilgimi çeker.",
    6: "Zaman sınırlamaları altında daha iyi çalışırım.",
    7: "Karar verirken dikkatli ve temkinliyimdir.",
    8: "Kalabalık ortamlarda bulunmak beni canlandırır.",
    9: "Mantıklı insanlara daha çok ilgi duyarım.",
   10: "Gerçek ve somut olaylar daha çok ilgimi çeker.",
   11: "Durumları değerlendirirken yasalara göre karar veririm.",
   12: "İnsanlara yaklaşımım genellikle nesneldir.",
   13: "Dakik biri olduğumu söyleyebilirim.",
   14: "Tamamlanmamış işler beni rahatsız eder.",
   15: "Sosyal çevremdeki gelişmeleri takip ederim.",
   16: "Günlük işleri genellikle kendi yöntemimle yaparım.",
   17: "Yazarların net ve doğrudan olmaları gerektiğini düşünürüm.",
   18: "Tutarlı düşünceler benim için daha önemlidir.",
   19: "Mantıklı kararlar vermekte daha rahat hissederim.",
   20: "Netlik ve kararlılık benim için önemlidir.",
   21: "Ciddi ve kararlı biriyimdir.",
   22: "Telefon görüşmeleri öncesinde ne söyleyeceğimi planlamam.",
   23: "Gerçeklerin kendini ifade ettiğine inanırım.",
   24: "Vizyoner insanlar bana ilham verir.",
   25: "Sakin kalabilen biri olduğumu düşünüyorum.",
   26: "Adaletsizlik, acımasızlıktan daha kötüdür.",
   27: "Olayların planlı şekilde gelişmesini tercih ederim.",
   28: "Bir ürünü satın aldığımda daha memnun hissederim.",
   29: "Topluluklarda ilk konuşmayı genellikle ben başlatırım.",
   30: "Sağduyu bazen sorgulanmalıdır.",
   31: "Çocuklar bazen hayal gücünü yeterince kullanamaz.",
   32: "Karar alırken standartlara göre hareket ederim.",
   33: "Kararlı ve net biriyimdir.",
   34: "Organize olmak benim için hayranlık uyandırıcıdır.",
   35: "Açık fikirli olmayı değerli bulurum.",
   36: "Yeni ve farklı insanlarla tanışmak bana enerji verir.",
   37: "Pratik bir insan olduğumu düşünürüm.",
   38: "Başkalarının bakış açısını öğrenmeyi tercih ederim.",
   39: "Bir konuyu detaylıca tartışmak daha tatmin edicidir.",
   40: "Kurallar benim davranışlarımı yönlendirir.",
   41: "Adil biri olmaya eğilimliyimdir.",
   42: "Her şeyin düzenli olmasını tercih ederim.",
   43: "İlişkilerde çoğu şey yeniden değerlendirilebilir olmalıdır.",
   44: "Telefon çaldığında ilk ben cevaplamak isterim.",
   45: "Gerçeklik duygumla gurur duyarım.",
   46: "Temel bilgiler ilgimi daha çok çeker.",
   47: "Çok duygusal olmak büyük bir hata olabilir.",
   48: "Gerçekçi biri olarak kendimi tanımlarım.",
   49: "Yapılandırılmış planları olan durumlar bana daha cazip gelir.",
   50: "Kısa süreli ama çok arkadaşlık kurmayı severim.",
   51: "İlkeler doğrultusunda hareket ederim.",
   52: "Üretim ve dağıtım süreçleri ilgimi çeker.",
   53: "Mantıklı biri olarak anılmak gurur vericidir.",
   54: "Kendimde en çok sadakati değerli bulurum.",
   55: "Kesin ve değişmez ifadelere daha çok güvenirim.",
   56: "Karar verdikten sonra kendimi daha rahat hissederim.",
   57: "Yeni insanlarla kolayca ve uzun uzun konuşabilirim.",
   58: "Tecrübeye daha çok güvenirim.",
   59: "Pratik düşünmeye daha yakınım.",
   60: "Açık ve net bir neden daha değerlidir.",
   61: "Empatik biri olmaya eğilimliyim.",
   62: "Bazen olayların akışına bırakılması gerektiğini düşünürüm.",
   63: "İlişkilerde koşullara göre karar veririm.",
   64: "Telefon çalınca genelde başkasının açmasını beklerim.",
   65: "Hayal gücümle övünürüm.",
   66: "Soyut fikirler ilgimi çeker.",
   67: "Duygularla hareket etmek hata olabilir.",
   68: "Kendimi daha çok mantıklı biri olarak görürüm.",
   69: "Planlı programlı durumları tercih ederim.",
   70: "Rutinler bana güven verir.",
   71: "İnsanlara yaklaşmam genellikle kolaydır.",
   72: "Mecazlı yazıları daha çok severim.",
   73: "Başkalarının duygularını anlamakta zorlanmam.",
   74: "Mantıklı düşünebilmek, merhametten daha önemlidir.",
   75: "Eleştiriye açık olmak, seçici olmaktan daha değerlidir.",
   76: "Planlı olayları tercih ederim.",
   77: "Planlı hareket etmek bana daha uygundur."
}


# ------- 3) Dinamik olarak 77 endpoint oluştur
def add_question_endpoint(q_no: int, text: str):
    async def answer_question(
        payload: SurveyAnswer,
        db: Session = Depends(get_db)
    ):
        resp = db.query(SurveyResponse).get(payload.respondent_id)
        if not resp:
            raise HTTPException(status_code=404, detail="Katılımcı bulunamadı")
        if getattr(resp, f"q{q_no}") is not None:
            raise HTTPException(status_code=400, detail="Bu soruya zaten cevap verdiniz")

        setattr(resp, f"q{q_no}", payload.answer)
        db.commit()
        return {"message": f"{q_no}. soru kaydedildi → {payload.answer}"}

    router.add_api_route(
        f"/q{q_no}",
        answer_question,
        methods=["POST"],
        response_model=Message,
        summary=f"{q_no}. {text}"
    )

for no, txt in QUESTIONS.items():
    add_question_endpoint(no, txt)
