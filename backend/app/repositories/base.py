from abc import ABC, abstractmethod

from app.models.schemas import DashboardStats, PalletMovement, PalletMovementCreate, StockReportItem


class AbstractPalletRepository(ABC):
    @abstractmethod
    def get_dashboard(self) -> DashboardStats:
        raise NotImplementedError

    @abstractmethod
    def list_pallet_movements(self) -> list[PalletMovement]:
        raise NotImplementedError

    @abstractmethod
    def create_pallet_movement(self, payload: PalletMovementCreate) -> PalletMovement:
        raise NotImplementedError

    @abstractmethod
    def get_pallet_movement(self, movement_id: str) -> PalletMovement | None:
        raise NotImplementedError

    @abstractmethod
    def get_stock_report(self) -> list[StockReportItem]:
        raise NotImplementedError
