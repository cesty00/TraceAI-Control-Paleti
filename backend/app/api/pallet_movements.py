from fastapi import APIRouter, HTTPException

from app.models.schemas import MovementStatus, PalletMovement, PalletMovementCreate, ValidationResult
from app.services.demo_data import PALLET_MOVEMENTS, next_movement_id
from app.services.validation import validate_movement

router = APIRouter(prefix="/api/pallet-movements", tags=["pallet-movements"])


@router.get("", response_model=list[PalletMovement])
def list_pallet_movements() -> list[PalletMovement]:
    return PALLET_MOVEMENTS


@router.post("", response_model=PalletMovement, status_code=201)
def create_pallet_movement(payload: PalletMovementCreate) -> PalletMovement:
    validation = validate_movement(payload)
    status = MovementStatus.VALIDATED if validation.valid else MovementStatus.ERROR
    movement = PalletMovement(id=next_movement_id(), status=status, **payload.model_dump())
    PALLET_MOVEMENTS.append(movement)
    return movement


@router.post("/{movement_id}/validate", response_model=ValidationResult)
def validate_existing_pallet_movement(movement_id: str) -> ValidationResult:
    movement = next((item for item in PALLET_MOVEMENTS if item.id == movement_id), None)
    if movement is None:
        raise HTTPException(status_code=404, detail="Movement not found")
    return validate_movement(PalletMovementCreate(**movement.model_dump(exclude={"id", "status"})))
