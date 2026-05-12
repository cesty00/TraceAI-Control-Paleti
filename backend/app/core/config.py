from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "TraceAI Control - Gestionare Paleti"
    environment: str = "mvp-demo"
    version: str = "0.2.0"
    production_integrations_enabled: bool = False
    database_url: str | None = None
    database_echo: bool = False

    @property
    def database_enabled(self) -> bool:
        return bool(self.database_url)


settings = Settings()
