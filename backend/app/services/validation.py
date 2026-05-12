from app.models.schemas import MovementType, PalletMovementCreate, ValidationResult

SOURCE_REQUIRED = {
    MovementType.INTERNAL_TRANSFER,
    MovementType.PRODUCTION_ALLOCATION,
    MovementType.PRODUCTION_CONFIRMATION,
    MovementType.DELIVERY,
    MovementType.SUPPLIER_RETURN,
    MovementType.DAMAGE,
    MovementType.REPAIR,
    MovementType.SCRAP,
    MovementType.ADJUSTMENT,
}

TARGET_REQUIRED = {
    MovementType.RECEPTION,
    MovementType.INTERNAL_TRANSFER,
    MovementType.PRODUCTION_ALLOCATION,
    MovementType.CUSTOMER_RETURN,
    MovementType.DAMAGE,
    MovementType.REPAIR,
    MovementType.ADJUSTMENT,
}


def validate_movement(payload: PalletMovementCreate) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    if payload.quantity <= 0:
        errors.append("quantity must be greater than 0")
    if not payload.pallet_code:
        errors.append("pallet_code is required")
    if not payload.movement_type:
        errors.append("movement_type is required")
    if payload.movement_type in SOURCE_REQUIRED and not payload.source_location:
        errors.append("source_location is required for this movement_type")
    if payload.movement_type in TARGET_REQUIRED and not payload.target_location:
        errors.append("target_location is required for this movement_type")
    if payload.movement_type in {MovementType.PRODUCTION_ALLOCATION, MovementType.PRODUCTION_CONFIRMATION} and not payload.production_order:
        warnings.append("production_order is recommended for production movements")

    return ValidationResult(valid=not errors, warnings=warnings, errors=errors)
