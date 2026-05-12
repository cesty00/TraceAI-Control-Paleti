from fastapi import APIRouter

from app.models.schemas import DashboardStats
from app.services.repository_factory import get_repository

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("", response_model=DashboardStats)
def get_dashboard() -> DashboardStats:
    return get_repository().get_dashboard()
