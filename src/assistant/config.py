"""Configuration App, read from enviroment variables or from .env"""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    llm_provider: Literal["ollama", "azure_openai", "bedrock"] = "ollama"
    chat_model: str = "qwen3:8b"
    embedding_model: str = "nomic-embed-text"
    ollama_url: str = "http://localhost:11434"
    chroma_dir: str = "data/chroma_db"
    database_path: str = "data/company.db"
    log_level: str = "INFO"
    log_dir: str = "logs"


@lru_cache
def get_settings() -> Settings:
    """Devuelve la configuración (se lee una sola vez)."""
    return Settings()
