from __future__ import annotations
import os
import json
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

# Suporta DATABASE_URL injetada pelo Docker Compose ou fallback local
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://buscapc:buscapc_secret@db:5432/buscapc"
)

# Se rodando fora do docker e o db:5432 não estiver acessível, permite fallback seguro
LOCAL_POSTGRES_FALLBACK = "postgresql+asyncpg://buscapc:buscapc_secret@localhost:5442/buscapc"
SQLITE_FALLBACK = "sqlite+aiosqlite:///./buscapc_local.db"

def get_engine_url() -> str:
    # Se estiver rodando dentro de container (ex: host 'db'), usa DATABASE_URL
    if os.getenv("RUNNING_IN_DOCKER") == "true" or "db:5432" in DATABASE_URL:
        return DATABASE_URL
    # Se uma URL explícita foi definida no ambiente
    if "POSTGRES_HOST" in os.environ:
        host = os.environ["POSTGRES_HOST"]
        port = os.environ.get("POSTGRES_PORT", "5432")
        user = os.environ.get("POSTGRES_USER", "buscapc")
        pw = os.environ.get("POSTGRES_PASSWORD", "buscapc_secret")
        db = os.environ.get("POSTGRES_DB", "buscapc")
        return f"postgresql+asyncpg://{user}:{pw}@{host}:{port}/{db}"
    return DATABASE_URL

engine = create_async_engine(
    get_engine_url(),
    echo=False,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
