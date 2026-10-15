from app.core.config import settings
from fastapi import FastAPI

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Virtual Store Engine with AI Agent and Budget Matcher",
)


@app.get("/")
async def root():
    return {
        "status": "varm-motor-online",
        "developer": "Milton - Senior Engineer",
        "destination": "Okinawa 🇯🇵",
    }
