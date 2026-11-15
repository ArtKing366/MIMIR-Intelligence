from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.session import engine, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(
    title=settings.app_name,
    description="AI-powered IT Service Desk & Incident Intelligence Platform",
    version="0.1.0",
    debug=settings.debug,
    lifespan=lifespan,
)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "application": "MIMIR Intelligence",
    }


@app.get("/health/database")
async def database_health(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))

    return {
        "database": "connected",
        "result": result.scalar_one(),
    }