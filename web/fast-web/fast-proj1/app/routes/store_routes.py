from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.dependencies import database_connection
from app.entities.dbstore import DbStore

store_router = APIRouter(prefix="/store", tags=["store"])


@store_router.post("/create", )
def create_book(db_store: DbStore, db: Session = Depends(database_connection)):
    db.add(db_store)
    db.commit()
    db.refresh(db_store)

    return ""
