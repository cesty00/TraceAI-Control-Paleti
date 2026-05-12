# API Contract MVP

## GET /health

Returneaza statusul aplicatiei.

Raspunsul include si modul de persistenta:

```json
{
  "status": "ok",
  "app": "TraceAI Control - Gestionare Paleti",
  "environment": "mvp-demo",
  "production_integrations_enabled": false,
  "database_enabled": false,
  "database_mode": "demo"
}
```

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

Cand `DATABASE_URL` este configurat, raspunsul este calculat din PostgreSQL; altfel foloseste date demo.

## GET /api/pallet-movements

Returneaza lista miscarilor demo sau, daca persistenta este activa, miscarile din PostgreSQL.

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

In modul PostgreSQL, codurile de palet, locatie si partener trebuie sa existe in master-data.

## POST /api/pallet-movements/{id}/validate

Valideaza o miscare existenta.

## GET /api/reports/stock

Returneaza raportul demo de stoc sau snapshot-ul din PostgreSQL, in functie de configuratia backend-ului.

## Endpointuri viitoare neimplementate

- `POST /api/sync/erp/{movement_id}`
- `POST /api/sync/wms/{movement_id}`
- `POST /api/sync/wme/{movement_id}`
- `GET /api/partner-balances`
