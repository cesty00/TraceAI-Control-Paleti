# Specificatie tehnica MVP

## Arhitectura

```text
Frontend React/Vite -> Backend FastAPI -> date demo in-memory
```

## Module

- Dashboard
- Miscari paleti
- Rapoarte stoc
- Validari minime
- Documentatie integrare ERP/WMS/WME

## Tipuri miscari

- RECEPTION
- INTERNAL_TRANSFER
- PRODUCTION_ALLOCATION
- PRODUCTION_CONFIRMATION
- DELIVERY
- CUSTOMER_RETURN
- SUPPLIER_RETURN
- DAMAGE
- REPAIR
- SCRAP
- ADJUSTMENT

## Statusuri

- DRAFT
- VALIDATED
- SYNC_PENDING
- PARTIAL_SYNC
- SYNCED
- ERROR
- CANCELLED

## Reguli MVP

- cantitatea trebuie sa fie mai mare decat zero;
- codul paletului este obligatoriu;
- tipul miscarii este obligatoriu;
- sursa/destinatia sunt obligatorii in functie de tipul miscarii.

## Limitari

- fara autentificare;
- fara baza de date activa;
- fara conectori reali ERP/WMS/WME;
- fara productie/release/daily-use.
