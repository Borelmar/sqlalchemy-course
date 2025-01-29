from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, text, URL
from config import settings

async_engine = None 

def init_db():
    global async_engine
    async_engine = create_async_engine(
        url=settings.DATABASE_URL_asyncpg,
        echo=True
    )

async def test():
    if async_engine != None:
        async with async_engine.connect() as conn:
            res = await conn.execute(text("SELECT 1;"))
            for row in res:
                print(row)
    else:
        raise 'async_engine is None'