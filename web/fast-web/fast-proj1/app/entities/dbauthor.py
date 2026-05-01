from typing import Optional

from sqlmodel import Field, Relationship, SQLModel
from dataclasses import dataclass
import datetime
from app.entities.db_store_book_author import DbBooksAuthor


@dataclass
class DbAuthor(SQLModel, table=True):
    __tablename__ = "author"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=40, default=None, index=True, unique=True)
    books: list["DbBooks"] = Relationship(back_populates="authors", link_model=DbBooksAuthor)

    created_at: datetime.datetime = Field(default=datetime.datetime.now(tz=datetime.timezone.utc))
    created_by: str = Field(default="system")
    updated_at: datetime.datetime = Field(default=datetime.datetime.now(tz=datetime.timezone.utc))
    updated_by: str = Field(default="system")

