from fastapi import APIRouter

from app.models.schemas import StockReportItem
from app.services.demo_data import STOCK_REPORT

router = APIRouter(prefix="/api/reports", tags=["reports"])


@router.get("/stock", response_model=list[StockReportItem])
def get_stock_report() -> list[StockReportItem]:
    return STOCK_REPORT
