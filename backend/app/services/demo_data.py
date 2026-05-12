from app.models.schemas import DashboardStats, MovementStatus, MovementType, PalletMovement, StockReportItem

DASHBOARD = DashboardStats(
    good_pallets=842,
    production_pallets=136,
    customer_pallets=428,
    damaged_pallets=39,
    sync_errors=0,
)

PALLET_MOVEMENTS: list[PalletMovement] = [
    PalletMovement(
        id="PAL-MOV-0001",
        movement_type=MovementType.RECEPTION,
        pallet_code="PAL-EUR-1200x800",
        quantity=64,
        source_location="ERP_RECEPTIE_FURNIZOR",
        target_location="WMS_PALETI_BUNI",
        partner_code="SUP-LEMN-NORD",
        reference_document="REC-2026-0001",
        reference_system="ERP",
        status=MovementStatus.SYNCED,
    ),
    PalletMovement(
        id="PAL-MOV-0002",
        movement_type=MovementType.PRODUCTION_ALLOCATION,
        pallet_code="PAL-EUR-1200x800",
        quantity=28,
        source_location="WMS_PALETI_BUNI",
        target_location="WME_LINIE_AMBALARE",
        production_order="PRD-4581",
        reference_document="WME-4581",
        reference_system="WME",
        status=MovementStatus.VALIDATED,
    ),
]

STOCK_REPORT: list[StockReportItem] = [
    StockReportItem(pallet_code="PAL-EUR-1200x800", location_code="WMS_PALETI_BUNI", quantity=842, state="GOOD"),
    StockReportItem(pallet_code="PAL-EUR-1200x800", location_code="WME_LINIE_AMBALARE", quantity=136, state="PRODUCTION"),
    StockReportItem(pallet_code="PAL-NON-STD", location_code="ERP_SOLD_CLIENTI", quantity=428, state="CUSTOMER"),
    StockReportItem(pallet_code="PAL-DETERIORAT", location_code="WMS_PALETI_DETERIORATI", quantity=39, state="DAMAGED"),
]


def next_movement_id() -> str:
    return f"PAL-MOV-{len(PALLET_MOVEMENTS) + 1:04d}"
