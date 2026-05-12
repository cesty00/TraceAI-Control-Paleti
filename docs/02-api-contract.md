# API Contract MVP

## GET /health

Returneaza statusul aplicatiei.

## GET /api/dashboard

```json
{
  "good_pallets": 842,
  "production_pallets": 136,
  "customer_pallets": 428,
  "damaged_pallets": 39,
  "sync_errors": 0
}
```

## GET /api/pallet-movements

Returneaza lista miscarilor demo.

## POST /api/pallet-movements

```json
{
  "movement_type": "RECEPTION",
  "pallet_code": "PAL-EUR-1200x800",
  "quantity": 10,
  "target_location": "WMS_PALETI_BUNI",
  "partner_code": "SUP-LEMN-NORD",
  "reference_document": "REC-2026-0001",
  "reference_system": "ERP"
}
```

## POST /api/pallet-movements/{id}/validate

Valideaza o miscare existenta.

## GET /api/reports/stock

Returneaza raportul demo de stoc.

## Endpointuri viitoare neimplementate

- `POST /api/sync/erp/{movement_id}`
- `POST /api/sync/wms/{movement_id}`
- `POST /api/sync/wme/{movement_id}`
- `GET /api/partner-balances`
