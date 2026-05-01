import datetime
from dataclasses import field
from typing import Optional

from pydantic import BaseModel, Field


class UpdateBooks(BaseModel):
    id: Optional[int]
    title: str
    price: float
    description: str
    created_at: datetime.datetime
    created_by: str
    updated_at: datetime.datetime
    updated_by: str
    authors: Optional[list] = field(default_factory=list([]))
    stores: Optional[list] = field(default_factory=list([]))

    def __init__(self, **data):
        super().__init__(**data)


class BookResponse(BaseModel):
    id: int
    title: str
    price: float
    description: str
    created_at: datetime.datetime
    created_by: str
    updated_at: datetime.datetime
    updated_by: str
    authors: Optional[list] = field(default_factory=list([]))
    stores: Optional[list] = field(default_factory=list([]))

    def __init__(self, **data):
        super().__init__(**data)
