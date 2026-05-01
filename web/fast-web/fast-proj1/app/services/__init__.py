import datetime

import jwt
from decouple import config
from fastapi import Header, HTTPException

from app.models.jwt_model import JwtTokenString, JwtToken
from app.models.login_model import Login


def get_token_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    else:
        print(f"header token {x_token}")
        return True


def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
    else:
        print(f"query token {token}")


def create_jwt_token(user: Login):
    payload = {
        "username": user.username,
        "exp": datetime.datetime.now(tz=datetime.timezone.utc)
        + datetime.timedelta(hours=2),
        "iat": datetime.datetime.now(tz=datetime.timezone.utc),
        "iss": "application",
    }

    jwt_token = jwt.encode(payload, config("secret_key"), algorithm="HS256")
    return jwt_token


def decode_jwt_token(token: JwtTokenString):
    print(f"got this token {token}")
    try:
        decoded_token = jwt.decode(
            token.token,
            config("secret_key"),
            algorithms=["HS256"],
            issuer="application",
            options={"verify_exp": True},
        )

        expiry_date_utc = datetime.datetime.fromtimestamp(
            int(decoded_token["exp"]), tz=datetime.timezone.utc
        )
        payload: JwtToken = JwtToken()

        payload.username = decoded_token["username"]
        payload.expiry = expiry_date_utc
        payload.issued_at = datetime.datetime.fromtimestamp(
            int(decoded_token["iat"]), tz=datetime.timezone.utc
        )
        payload.issuer = decoded_token["iss"]

        return payload
    except BaseException as e:
        return e
