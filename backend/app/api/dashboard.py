from fastapi import APIRouter

from app.models.schemas import DashboardStats
from app.services.demo_data import DASHBOARD

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("", response_model=DashboardStats)
def get_dashboard() -> DashboardStats:
    return DASHBOARD
