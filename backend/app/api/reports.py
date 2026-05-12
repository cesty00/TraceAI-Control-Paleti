from fastapi import APIRouter

from app.models.schemas import StockReportItem
from app.services.repository_factory import get_repository

router = APIRouter(prefix="/api/reports", tags=["reports"])


@router.get("/stock", response_model=list[StockReportItem])
def get_stock_report() -> list[StockReportItem]:
    return get_repository().get_stock_report()
