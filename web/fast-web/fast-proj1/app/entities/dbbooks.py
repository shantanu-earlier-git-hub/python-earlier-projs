from dataclasses import dataclass
from typing import Optional
import datetime
from sqlmodel import Field, Relationship, SQLModel

from app.entities.db_store_book_author import DbBooksAuthor, DbBooksStore


@dataclass
class DbBooks(SQLModel, table=True):
    __tablename__ = "books"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: str = Field(default=None, index=True, nullable=False)
    price: float = Field(default=None, index=True, nullable=False)
    description: str = Field(default=None)

    created_at: datetime.datetime = Field(default=datetime.datetime.now(tz=datetime.timezone.utc))
    created_by: str = Field(default="system")
    updated_at: datetime.datetime = Field(default=datetime.datetime.now(tz=datetime.timezone.utc))
    updated_by: str = Field(default="system")

    authors: Optional[list["DbAuthor"]] = Relationship(back_populates="books", link_model=DbBooksAuthor)
    stores: Optional[list["DbStore"]] = Relationship(back_populates="books", link_model=DbBooksStore)
