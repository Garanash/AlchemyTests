import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text, String
from typing import Annotated

from config import setting

sync_engine = create_engine(
    url=setting.DATABASE_URL_sqlite,
    echo=True,
    # pool_size=50,
    # max_overflow=10,
)

async_engine = create_async_engine(
    url=setting.DATABASE_URL_aiosqlite,
    echo=True,
    # pool_size=50,
    # max_overflow=10,
)

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }
