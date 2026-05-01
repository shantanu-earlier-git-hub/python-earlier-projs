from dataclasses import dataclass
import datetime

from app.models import BaseResponse


@dataclass
class JwtTokenString(BaseResponse):
    username: str
    token: str


@dataclass
class JwtToken(BaseResponse):
    username: str
    expiry: datetime.datetime
    issued_at: datetime.datetime
    issuer: str
