from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from dataclasses import dataclass
import datetime

from app.entities.db_store_book_author import DbBooksStore


@dataclass
class DbStore(SQLModel, table=True):
    __tablename__ = "store"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(default=None)
    created_at: datetime.datetime = Field(default=datetime.datetime.now(tz=datetime.timezone.utc))
    created_by: str = Field(default="system")
    updated_at: datetime.datetime = Field(default=datetime.datetime.now(tz=datetime.timezone.utc))
    updated_by: str = Field(default="system")

    books: list["DbBooks"] = Relationship(back_populates="stores", link_model=DbBooksStore)

