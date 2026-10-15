from fastapi import FastAPI

app = FastAPI(
    title="varm-ai-store-backend",
    description="Motor de Tienda Virtual con Agente de IA y Cotizador Inteligente - Arquitectura Premium",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "status": "varm-motor-online",
        "developer": "Milton - Senior Engineer",
        "location": "Puerto Asís -> Okinawa 🇯🇵",
    }
