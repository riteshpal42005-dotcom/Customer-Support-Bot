from pydantic import BaseModel
from datetime import datetime

class ChatMessageCreate(BaseModel):
    message: str

class ChatMessageResponse(BaseModel):
    id: int
    message: str
    sender_id: int
    created_at: datetime

    class Config:
        from_attributes = True
