from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import uRL, create_engine, text
from config import db_settings
import asyncio

async_engine = create_async_engine(
    url=db_settings.DATABASE_URL_asyncpg,
    echo=True
)

async def test():
    async with async_engine() as conn:
        res = await conn.execute(text("SELECT 1;"))
        print(res.first())

asyncio.run(test())
