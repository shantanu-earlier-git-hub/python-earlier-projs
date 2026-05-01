from dataclasses import dataclass
import datetime


@dataclass
class Audit:
    createdAt: datetime.datetime
    updatedAt: datetime.datetime
    created_by: str
    updated_by: str


@dataclass
class BaseResponse(Audit):
    status: str
    message: str


@dataclass
class AppException(Exception):
    error_code: int
    message: str
    status_code: int = 500
    object: object = None
