# pyrefly: ignore [missing-import]
from fastapi import APIRouter

from schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest) -> ChatResponse:

    return ChatResponse(
        success=True,
        response="Hello! Could you share your registered mobile number?"
    )