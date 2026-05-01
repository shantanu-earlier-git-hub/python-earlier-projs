from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlmodel import Session, select

from app.dependencies import database_connection
from app.entities.dbbooks import DbBooks
from app.models.books_model import BookResponse, UpdateBooks

books_router = APIRouter(prefix="/books", tags=["books"])


# create a book
@books_router.post("/create", response_model=BookResponse)
def create_book(db_book: DbBooks, db: Session = Depends(database_connection)):
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    if db_book:
        response = BookResponse(**db_book.model_dump(), authors=[], stores=[])
        book = response
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Some Error Occurred",
        )

    return book


@books_router.get("/all", response_model=list[BookResponse])
def find_all(session: Session = Depends(database_connection)):
    book_list: list[BookResponse] = list([])
    books_found = session.scalars(select(DbBooks)).all()

    if books_found:
        for book in books_found:
            book_list.append(BookResponse(**book.model_dump(), authors=[], stores=[]))
    elif not books_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Some Error Occurred",
        )

    return book_list


@books_router.get("/{book_id}", response_model=BookResponse)
def find_by_book_id(book_id: int, session: Session = Depends(database_connection)):
    books_found = session.get(DbBooks, book_id)
    if not books_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    else:
        books_found = BookResponse(**books_found.model_dump(), authors=[], stores=[])

    return books_found


@books_router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(database_connection)):
    books_found = session.get(DbBooks, book_id)

    if not books_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    else:
        session.delete(books_found)
        session.commit()

    return f"Book {book_id} deleted"


@books_router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, updated_book: UpdateBooks, session: Session = Depends(database_connection)):
    books_found = session.get(DbBooks, book_id)

    if not books_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    else:
        for field, value in updated_book.model_dump().items():
            setattr(books_found, field, value)

        session.commit()
        session.refresh(books_found)

    return BookResponse(**books_found.model_dump(), authors=[], stores=[])
