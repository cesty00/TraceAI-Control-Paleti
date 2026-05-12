from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class PalletItem(Base):
    __tablename__ = "pallet_items"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    pallet_code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    unit: Mapped[str] = mapped_column(String(20), nullable=False)
    pallet_type: Mapped[str | None] = mapped_column(String(50))


class Location(Base):
    __tablename__ = "locations"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    location_code: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    system_owner: Mapped[str] = mapped_column(String(20), nullable=False)
    location_type: Mapped[str] = mapped_column(String(50), nullable=False)


class Partner(Base):
    __tablename__ = "partners"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    partner_code: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    partner_type: Mapped[str] = mapped_column(String(20), nullable=False)


class PalletMovementRecord(Base):
    __tablename__ = "pallet_movements"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    movement_no: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    movement_type: Mapped[str] = mapped_column(String(50), nullable=False)
    pallet_item_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("pallet_items.id"), nullable=False)
    quantity: Mapped[float] = mapped_column(Numeric(12, 3), nullable=False)
    source_location_id: Mapped[str | None] = mapped_column(UUID(as_uuid=False), ForeignKey("locations.id"))
    target_location_id: Mapped[str | None] = mapped_column(UUID(as_uuid=False), ForeignKey("locations.id"))
    partner_id: Mapped[str | None] = mapped_column(UUID(as_uuid=False), ForeignKey("partners.id"))
    production_order: Mapped[str | None] = mapped_column(String(100))
    reference_document: Mapped[str | None] = mapped_column(String(100))
    reference_system: Mapped[str | None] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(30), nullable=False)
    error_message: Mapped[str | None] = mapped_column(Text)
    metadata_json: Mapped[dict] = mapped_column("metadata", JSONB, nullable=False, default=dict)
    created_by: Mapped[str | None] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())


class StockSnapshot(Base):
    __tablename__ = "pallet_stock_snapshot"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    pallet_item_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("pallet_items.id"), nullable=False)
    location_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("locations.id"), nullable=False)
    quantity: Mapped[float] = mapped_column(Numeric(12, 3), nullable=False)
    source_system: Mapped[str] = mapped_column(String(20), nullable=False)
    snapshot_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())


class SyncLog(Base):
    __tablename__ = "sync_log"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    movement_id: Mapped[str | None] = mapped_column(UUID(as_uuid=False), ForeignKey("pallet_movements.id"))
    target_system: Mapped[str] = mapped_column(String(20), nullable=False)
    sync_status: Mapped[str] = mapped_column(String(30), nullable=False)
    error_message: Mapped[str | None] = mapped_column(Text)
