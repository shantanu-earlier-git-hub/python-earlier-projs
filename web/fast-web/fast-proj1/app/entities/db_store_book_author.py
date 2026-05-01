from dataclasses import dataclass

from sqlmodel import SQLModel, Field


@dataclass
class DbBooksStore(SQLModel, table=True):
    __tablename__ = "books_store"

    book_id: int = Field(default=None, foreign_key="books.id", primary_key=True)
    store_id: int = Field(default=None, foreign_key="store.id", primary_key=True)


@dataclass
class DbBooksAuthor(SQLModel, table=True):
    __tablename__ = "books_author"

    book_id: int = Field(default=None, foreign_key="books.id", primary_key=True)
    author_id: int = Field(default=None, foreign_key="author.id", primary_key=True)
