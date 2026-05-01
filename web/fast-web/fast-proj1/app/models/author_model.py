import datetime
from dataclasses import dataclass, field
from typing import Optional

from pydantic import BaseModel


class UpdateAuthor(BaseModel):
    id: Optional[int]
    name: str
    created_at: datetime.datetime
    created_by: str
    updated_at: datetime.datetime
    updated_by: str

    def __init__(self, **data):
        super().__init__(**data)


class AuthorResponse(BaseModel):
    id: int
    name: str
    created_at: datetime.datetime
    created_by: str
    updated_at: datetime.datetime
    updated_by: str

    books: Optional[list] = field(default_factory=list)

    def __init__(self, **data):
        super().__init__(**data)
