# from fastapi import APIRouter
# from fastapi.params import Depends
#
# from app.bak.auth import create_jwt_token, decode_jwt_token
# from app.bak.models import Login, JwtToken
#
# router = APIRouter(
#     prefix="/login",
#     tags=["login"]
# )
#
#
#
# @router.get("/")
# async def get_login(user_token: Login = Depends(create_jwt_token)):
#     return f"got data {user_token}"
#
#
# @router.post("/signin")
# def verify_token(jwt_payload: JwtToken = Depends(decode_jwt_token)):
#     return f"decoded token ->  {jwt_payload}"
