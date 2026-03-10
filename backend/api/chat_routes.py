from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.agent_service import process_message

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str


@router.post("/chat")
def chat(req: ChatRequest):

    reply = process_message(req.user_id, req.message)

    return {"reply": reply}