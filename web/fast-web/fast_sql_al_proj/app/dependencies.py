from decouple import config
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

app = FastAPI()

async_engine = create_async_engine(config("database_url"),
                                   pool_pre_ping=True, pool_recycle=3600, pool_size=20)
AsyncSessionLocal = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
