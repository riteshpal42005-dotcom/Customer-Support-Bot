from fastapi import APIRouter

# pyrefly: ignore [missing-import]

router = APIRouter()

@router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}