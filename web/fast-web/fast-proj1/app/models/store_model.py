import dataclasses
import datetime
from dataclasses import field
from typing import Optional

from pydantic import BaseModel


class StoreResponse(BaseModel):
    id: int
    name: str
    created_at: datetime.datetime
    created_by: str
    updated_at: datetime.datetime
    updated_by: str

    books: list = field(default_factory=list)


class UpdateStore(BaseModel):
    id: Optional[int]
    name: str
    created_at: datetime.datetime
    created_by: str
    updated_at: datetime.datetime
    updated_by: str

    books: list = field(default_factory=list)
