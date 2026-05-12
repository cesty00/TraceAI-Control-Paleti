from app.models.schemas import DashboardStats, MovementStatus, PalletMovement, PalletMovementCreate, StockReportItem
from app.repositories.base import AbstractPalletRepository
from app.services.demo_data import DASHBOARD, PALLET_MOVEMENTS, STOCK_REPORT, next_movement_id
from app.services.validation import validate_movement


class DemoPalletRepository(AbstractPalletRepository):
    def get_dashboard(self) -> DashboardStats:
        return DASHBOARD

    def list_pallet_movements(self) -> list[PalletMovement]:
        return PALLET_MOVEMENTS

    def create_pallet_movement(self, payload: PalletMovementCreate) -> PalletMovement:
        validation = validate_movement(payload)
        status = MovementStatus.VALIDATED if validation.valid else MovementStatus.ERROR
        movement = PalletMovement(id=next_movement_id(), status=status, **payload.model_dump())
        PALLET_MOVEMENTS.append(movement)
        return movement

    def get_pallet_movement(self, movement_id: str) -> PalletMovement | None:
        return next((item for item in PALLET_MOVEMENTS if item.id == movement_id), None)

    def get_stock_report(self) -> list[StockReportItem]:
        return STOCK_REPORT
