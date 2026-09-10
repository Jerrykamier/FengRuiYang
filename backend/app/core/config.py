from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "University RAG Assistant"
    APP_VERSION: str = "0.1.0"
    ENV: str = "dev"

    DATABASE_URL: str = "sqlite:///./data/app.db"
    VECTOR_DB_DIR: str = "./data/vector_db"

    LLM_PROVIDER: str = "mock"
    LLM_MODEL_NAME: str = "mock-model"
    LLM_API_KEY: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
