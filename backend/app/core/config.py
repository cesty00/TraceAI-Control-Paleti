from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "TraceAI Control - Gestionare Paleti"
    environment: str = "mvp-demo"
    version: str = "0.1.0"
    production_integrations_enabled: bool = False


settings = Settings()
