from fastapi import APIRouter, HTTPException

from app.models.schemas import PalletMovement, PalletMovementCreate, ValidationResult
from app.services.repository_factory import get_repository
from app.services.validation import validate_movement

router = APIRouter(prefix="/api/pallet-movements", tags=["pallet-movements"])


@router.get("", response_model=list[PalletMovement])
def list_pallet_movements() -> list[PalletMovement]:
    return get_repository().list_pallet_movements()


@router.post("", response_model=PalletMovement, status_code=201)
def create_pallet_movement(payload: PalletMovementCreate) -> PalletMovement:
    try:
        return get_repository().create_pallet_movement(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/{movement_id}/validate", response_model=ValidationResult)
def validate_existing_pallet_movement(movement_id: str) -> ValidationResult:
    movement = get_repository().get_pallet_movement(movement_id)
    if movement is None:
        raise HTTPException(status_code=404, detail="Movement not found")
    return validate_movement(PalletMovementCreate(**movement.model_dump(exclude={"id", "status"})))
