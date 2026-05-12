from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.dashboard import router as dashboard_router
from app.api.pallet_movements import router as pallet_movements_router
from app.api.reports import router as reports_router
from app.core.config import settings

app = FastAPI(title=settings.app_name, version=settings.version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard_router)
app.include_router(pallet_movements_router)
app.include_router(reports_router)


@app.get("/health")
def health() -> dict[str, str | bool]:
    return {
        "status": "ok",
        "app": settings.app_name,
        "environment": settings.environment,
        "production_integrations_enabled": settings.production_integrations_enabled,
        "database_enabled": settings.database_enabled,
        "database_mode": "postgres" if settings.database_enabled else "demo",
    }
