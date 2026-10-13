"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Expense tracker Api"
    environment: str = "development"

    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_mintures: int = 30

    database_url: str
    log_level: str = "INFO"


settings = Settings()
