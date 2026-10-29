"""Unique point of models creation. Change of provider only touch this file."""

from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from langchain_ollama import ChatOllama, OllamaEmbeddings

from assistant.config import get_settings


def get_chat_model(temperature: float = 0.0) -> BaseChatModel:
    """Create the chat model configurated."""
    settings = get_settings()
    if settings.llm_provider == "ollama":
        return ChatOllama(
            model=settings.chat_model,
            base_url=settings.ollama_url,
            temperature=temperature,
            reasoning=False,
        )
    # Here would be AzureChatOpenAI (langchain-openai) or ChatBedrockConverse (langchain-aws).
    raise ValueError(f"Provider not supported yet: {settings.llm_provider}")


def get_embeddings() -> Embeddings:
    """Create the embedding model configurated."""
    settings = get_settings()
    return OllamaEmbeddings(model=settings.embedding_model, base_url=settings.ollama_url)
