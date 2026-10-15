# backend/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Configuración del Proyecto
    PROJECT_NAME: str = "varm-ai-store-backend"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Configuración de Base de Datos (PostgreSQL)
    # Dejamos valores por defecto para desarrollo local
    DB_SERVER: str = "localhost"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "varm_db"
    DB_PORT: str = "5432"

    # Configuración de Inteligencia Artificial (Próximamente)
    AI_PROVIDER_API_KEY: str = "placeholder_key"

    # Buscador automático del archivo .env en la raíz del backend
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )


# Instancia única para importar en todo el proyecto
settings = Settings()
