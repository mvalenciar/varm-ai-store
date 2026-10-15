# backend/tests/test_main.py
from app.main import app
from starlette.testclient import TestClient

# Inicializamos el cliente de pruebas nativo de FastAPI
client = TestClient(app)


def test_read_root_success():
    """
    Meticulous Test: Verify that the root endpoint starts successfully
    and returns the expected configuration metadata.
    """
    response = client.get("/")

    # Verificaciones estrictas (Assertions)
    assert response.status_code == 200
    assert response.json() == {
        "status": "varm-motor-online",
        "developer": "Milton - Senior Engineer",
        "destination": "Okinawa 🇯🇵",
    }
