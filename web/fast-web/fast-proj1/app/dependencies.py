from decouple import config
from sqlmodel import SQLModel, create_engine, Session
from contextlib import asynccontextmanager

from fastapi import FastAPI

engine = create_engine(config("database_url"))


def database_connection():
    with Session(engine, autocommit=False, autoflush=False) as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)
