from app.core.config import settings


def test_settings_load_env_variables():
    """
    Meticulous Test: Verify that Pydantic Settings correctly reads
    and overrides default configuration using the local .env file.
    """
    assert settings.PROJECT_NAME == "varm-ai-store-backend"
    assert settings.DB_PORT == "5432"
    assert isinstance(settings.DB_SERVER, str)
    assert settings.API_V1_STR == "/api/v1"
