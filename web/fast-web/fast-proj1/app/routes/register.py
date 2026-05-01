from fastapi import APIRouter
from app.models.login_model import Login

router = APIRouter(prefix="/register", tags=["register"])


@router.post("/signup")
async def register(user_token: Login):
    return f"got data {user_token}"
