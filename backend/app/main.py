from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    description="AI-powered IT Service Desk & Incident Intelligence Platform",
    version="0.1.0",
    debug=settings.debug,
)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "application": "MIMIR Intelligence",
    }