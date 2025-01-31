from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Computed, Index, text

class Base(DeclarativeBase):
    pass

class Vacancy(Base):
    __tablename__ = 'vacancies'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    body: Mapped[str] = mapped_column()

    search_vector: Mapped[str] = mapped_column(
        TSVECTOR,
        Computed("to_tsvector('russian', title || ' ' || body)", persisted=True)
    )

    __table_args__ = (
        Index("ix_vacancy_search", "search_vector", postgresql_using="gin"),
    )