from contextlib import asynccontextmanager

from app.dependencies import app, async_engine
from app.entities import Base


@asynccontextmanager
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Server is running")


@app.get("/")
async def home():
    return {"message": f"Hello World"}
