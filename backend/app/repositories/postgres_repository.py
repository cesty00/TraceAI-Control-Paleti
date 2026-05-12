from decimal import Decimal

from sqlalchemy import case, func, select
from sqlalchemy.orm import aliased, sessionmaker

from app.db.models import Location, PalletItem, PalletMovementRecord, Partner, StockSnapshot, SyncLog
from app.models.schemas import DashboardStats, MovementStatus, MovementType, PalletMovement, PalletMovementCreate, StockReportItem
from app.repositories.base import AbstractPalletRepository
from app.services.validation import validate_movement


class PostgresPalletRepository(AbstractPalletRepository):
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    def get_dashboard(self) -> DashboardStats:
        with self.session_factory() as session:
            totals = session.execute(
                select(
                    func.coalesce(func.sum(case((Location.location_type == "GOOD", StockSnapshot.quantity), else_=0)), 0),
                    func.coalesce(func.sum(case((Location.location_type == "PRODUCTION", StockSnapshot.quantity), else_=0)), 0),
                    func.coalesce(func.sum(case((Location.location_type == "CUSTOMER_BALANCE", StockSnapshot.quantity), else_=0)), 0),
                    func.coalesce(func.sum(case((Location.location_type == "DAMAGED", StockSnapshot.quantity), else_=0)), 0),
                )
                .select_from(StockSnapshot)
                .join(Location, StockSnapshot.location_id == Location.id)
            ).one()
            sync_errors = session.execute(
                select(func.count()).select_from(SyncLog).where(SyncLog.sync_status == "ERROR")
            ).scalar_one()

        return DashboardStats(
            good_pallets=self._int_value(totals[0]),
            production_pallets=self._int_value(totals[1]),
            customer_pallets=self._int_value(totals[2]),
            damaged_pallets=self._int_value(totals[3]),
            sync_errors=int(sync_errors),
        )

    def list_pallet_movements(self) -> list[PalletMovement]:
        source_location = aliased(Location)
        target_location = aliased(Location)

        with self.session_factory() as session:
            rows = session.execute(
                select(
                    PalletMovementRecord,
                    PalletItem.pallet_code,
                    source_location.location_code,
                    target_location.location_code,
                    Partner.partner_code,
                )
                .join(PalletItem, PalletMovementRecord.pallet_item_id == PalletItem.id)
                .outerjoin(source_location, PalletMovementRecord.source_location_id == source_location.id)
                .outerjoin(target_location, PalletMovementRecord.target_location_id == target_location.id)
                .outerjoin(Partner, PalletMovementRecord.partner_id == Partner.id)
                .order_by(PalletMovementRecord.created_at.desc(), PalletMovementRecord.movement_no.desc())
            ).all()

        return [
            self._to_schema(record, pallet_code, source_code, target_code, partner_code)
            for record, pallet_code, source_code, target_code, partner_code in rows
        ]

    def create_pallet_movement(self, payload: PalletMovementCreate) -> PalletMovement:
        validation = validate_movement(payload)
        status = MovementStatus.VALIDATED if validation.valid else MovementStatus.ERROR

        with self.session_factory() as session:
            pallet_item = self._require_pallet_item(session, payload.pallet_code)
            source_location = self._resolve_location(session, payload.source_location)
            target_location = self._resolve_location(session, payload.target_location)
            partner = self._resolve_partner(session, payload.partner_code)
            movement_no = self._next_movement_number(session)

            record = PalletMovementRecord(
                movement_no=movement_no,
                movement_type=payload.movement_type.value,
                pallet_item_id=pallet_item.id,
                quantity=payload.quantity,
                source_location_id=source_location.id if source_location else None,
                target_location_id=target_location.id if target_location else None,
                partner_id=partner.id if partner else None,
                production_order=payload.production_order,
                reference_document=payload.reference_document,
                reference_system=payload.reference_system,
                status=status.value,
                error_message="; ".join(validation.errors) if validation.errors else None,
                metadata_json={},
                created_by="api",
            )
            session.add(record)
            session.commit()
            session.refresh(record)

        return self._to_schema(
            record,
            pallet_item.pallet_code,
            source_location.location_code if source_location else None,
            target_location.location_code if target_location else None,
            partner.partner_code if partner else None,
        )

    def get_pallet_movement(self, movement_id: str) -> PalletMovement | None:
        source_location = aliased(Location)
        target_location = aliased(Location)

        with self.session_factory() as session:
            row = session.execute(
                select(
                    PalletMovementRecord,
                    PalletItem.pallet_code,
                    source_location.location_code,
                    target_location.location_code,
                    Partner.partner_code,
                )
                .join(PalletItem, PalletMovementRecord.pallet_item_id == PalletItem.id)
                .outerjoin(source_location, PalletMovementRecord.source_location_id == source_location.id)
                .outerjoin(target_location, PalletMovementRecord.target_location_id == target_location.id)
                .outerjoin(Partner, PalletMovementRecord.partner_id == Partner.id)
                .where(PalletMovementRecord.movement_no == movement_id)
            ).one_or_none()

        if row is None:
            return None

        record, pallet_code, source_code, target_code, partner_code = row
        return self._to_schema(record, pallet_code, source_code, target_code, partner_code)

    def get_stock_report(self) -> list[StockReportItem]:
        with self.session_factory() as session:
            rows = session.execute(
                select(
                    PalletItem.pallet_code,
                    Location.location_code,
                    StockSnapshot.quantity,
                    Location.location_type,
                )
                .join(PalletItem, StockSnapshot.pallet_item_id == PalletItem.id)
                .join(Location, StockSnapshot.location_id == Location.id)
                .order_by(Location.location_code, PalletItem.pallet_code)
            ).all()

        return [
            StockReportItem(
                pallet_code=pallet_code,
                location_code=location_code,
                quantity=float(quantity),
                state=state,
            )
            for pallet_code, location_code, quantity, state in rows
        ]

    def _require_pallet_item(self, session, pallet_code: str) -> PalletItem:
        item = session.execute(select(PalletItem).where(PalletItem.pallet_code == pallet_code)).scalar_one_or_none()
        if item is None:
            raise ValueError(f"Unknown pallet_code: {pallet_code}")
        return item

    def _resolve_location(self, session, location_code: str | None) -> Location | None:
        if not location_code:
            return None
        location = session.execute(select(Location).where(Location.location_code == location_code)).scalar_one_or_none()
        if location is None:
            raise ValueError(f"Unknown location_code: {location_code}")
        return location

    def _resolve_partner(self, session, partner_code: str | None) -> Partner | None:
        if not partner_code:
            return None
        partner = session.execute(select(Partner).where(Partner.partner_code == partner_code)).scalar_one_or_none()
        if partner is None:
            raise ValueError(f"Unknown partner_code: {partner_code}")
        return partner

    def _next_movement_number(self, session) -> str:
        current = session.execute(
            select(PalletMovementRecord.movement_no)
            .where(PalletMovementRecord.movement_no.like("PAL-MOV-%"))
            .order_by(PalletMovementRecord.movement_no.desc())
            .limit(1)
        ).scalar_one_or_none()
        if current is None:
            return "PAL-MOV-0001"
        try:
            next_number = int(current.split("-")[-1]) + 1
        except ValueError:
            count = session.execute(select(func.count()).select_from(PalletMovementRecord)).scalar_one()
            next_number = int(count) + 1
        return f"PAL-MOV-{next_number:04d}"

    def _to_schema(
        self,
        record: PalletMovementRecord,
        pallet_code: str,
        source_code: str | None,
        target_code: str | None,
        partner_code: str | None,
    ) -> PalletMovement:
        return PalletMovement(
            id=record.movement_no,
            movement_type=MovementType(record.movement_type),
            pallet_code=pallet_code,
            quantity=float(record.quantity),
            source_location=source_code,
            target_location=target_code,
            partner_code=partner_code,
            production_order=record.production_order,
            reference_document=record.reference_document,
            reference_system=record.reference_system,
            status=MovementStatus(record.status),
        )

    def _int_value(self, value: Decimal | int | float) -> int:
        return int(float(value))
