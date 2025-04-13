from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import setting

engine = create_engine(
    url=setting.DATABASE_URL_sqlite,
    echo=True,
    pool_size=50,
    max_overflow=10,
)

with engine.connect() as conn:
    res = conn.execute(text("SELECT sqlite_version()"))
    print(f"{res=}")