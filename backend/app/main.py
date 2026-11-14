from fastapi import FastAPI

app = FastAPI(
    title="MIMIR Intelligence API",
    description="AI-powered IT Service Desk & Incident Intelligence Platform",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "application": "MIMIR Intelligence",
    }