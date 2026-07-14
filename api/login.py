# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from env import ADMIN_NAME, ADMIN_PASSWORD
from schemas.login import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/login")
async def login(request: LoginRequest) -> LoginResponse:
    if request.username == ADMIN_NAME and request.password == ADMIN_PASSWORD:
        return {
            "success": True,
            "message": "Login successful",
        }
    
    return {
        "success": False,
        "message": "Invalid credentials",
    }
