from http.client import HTTPException

from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlmodel import Session, select

from app.dependencies import database_connection
from app.entities.dbauthor import DbAuthor
from app.models.author_model import AuthorResponse

author_router = APIRouter(prefix="/author", tags=["author"])


# create author
@author_router.post("/create", response_model=AuthorResponse)
def create_author(db_author: DbAuthor, db: Session = Depends(database_connection)):
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    if db_author:
        response = AuthorResponse(**db_author.model_dump(), books=[])
        book = response
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Some Error Occurred",
        )

    return book


# get all author
@author_router.get("/all", response_model=list[AuthorResponse])
def find_all(session: Session = Depends(database_connection)):
    author_list: list[AuthorResponse] = list([])
    author_found = session.scalars(select(DbAuthor)).all()

    if author_found:
        for book in author_found:
            author_list.append(AuthorResponse(**book.model_dump()))
    elif not author_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Some Error Occurred",
        )

    return author_list

# create many authors


# get author


# update author


# delete author
