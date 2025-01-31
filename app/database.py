from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.dialects.postgresql import to_tsquery, ts_headline
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import create_engine, text, URL, Boolean, select, MetaData, func
from config import settings
from models import Vacancy


async_engine = create_async_engine(url=settings.DATABASE_URL_asyncpg, echo=True)
sync_engine = create_engine(url=settings.DATABASE_URL_psycopg, echo=True)
async_session_factory = async_sessionmaker(async_engine)
metadata_obj = MetaData()

def create_schema():
    Vacancy.metadata.create_all(sync_engine, checkfirst=True)

async def search_vacancy(words: str):
    async with async_session_factory() as session:
        query = select(Vacancy).where(Vacancy.search_vector.op('@@')(to_tsquery('russian', words.replace(' ', ' & '))))
        result = await session.execute(query)
    return result.scalars().all()

async def add_vacancy(vacancy: Vacancy):
    async with async_session_factory() as session:
        session.add(vacancy)
        await session.commit()

async def get_all_vacancies():
    async with async_session_factory() as session:
        result = await session.execute(select(Vacancy))
        vacancies = result.scalars().all()
    return vacancies