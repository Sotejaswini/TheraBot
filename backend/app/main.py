from fastapi import FastAPI
from pydantic import BaseModel
from app.services.rag_service import get_rag_response
from app.services.safety import check_crisis_keywords

app = FastAPI(title="TheraBot API")

class ChatRequest(BaseModel):
    query: str
    session_id: str = "default"

@app.get("/health")
def health():
    return {"status": "ok", "service": "TheraBot API"}

@app.post("/chat")
def chat(req: ChatRequest):
    crisis_flag, helpline = check_crisis_keywords(req.query)
    response = get_rag_response(req.query, req.session_id)
    return {
        "response": response,
        "crisis_detected": crisis_flag,
        "helpline": helpline if crisis_flag else None
    }
