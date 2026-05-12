from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MovementType(str, Enum):
    RECEPTION = "RECEPTION"
    INTERNAL_TRANSFER = "INTERNAL_TRANSFER"
    PRODUCTION_ALLOCATION = "PRODUCTION_ALLOCATION"
    PRODUCTION_CONFIRMATION = "PRODUCTION_CONFIRMATION"
    DELIVERY = "DELIVERY"
    CUSTOMER_RETURN = "CUSTOMER_RETURN"
    SUPPLIER_RETURN = "SUPPLIER_RETURN"
    DAMAGE = "DAMAGE"
    REPAIR = "REPAIR"
    SCRAP = "SCRAP"
    ADJUSTMENT = "ADJUSTMENT"


class MovementStatus(str, Enum):
    DRAFT = "DRAFT"
    VALIDATED = "VALIDATED"
    SYNC_PENDING = "SYNC_PENDING"
    PARTIAL_SYNC = "PARTIAL_SYNC"
    SYNCED = "SYNCED"
    ERROR = "ERROR"
    CANCELLED = "CANCELLED"


class DashboardStats(BaseModel):
    good_pallets: int
    production_pallets: int
    customer_pallets: int
    damaged_pallets: int
    sync_errors: int


class PalletMovementCreate(BaseModel):
    movement_type: MovementType
    pallet_code: str = Field(..., min_length=1)
    quantity: float = Field(..., gt=0)
    source_location: Optional[str] = None
    target_location: Optional[str] = None
    partner_code: Optional[str] = None
    production_order: Optional[str] = None
    reference_document: Optional[str] = None
    reference_system: Optional[str] = None


class PalletMovement(PalletMovementCreate):
    id: str
    status: MovementStatus = MovementStatus.DRAFT


class ValidationResult(BaseModel):
    valid: bool
    warnings: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)


class StockReportItem(BaseModel):
    pallet_code: str
    location_code: str
    quantity: float
    state: str
