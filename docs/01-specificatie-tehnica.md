# Specificatie tehnica MVP

## Arhitectura

```text
Frontend React/Vite -> Backend FastAPI -> repository layer -> PostgreSQL optional / demo fallback
```

## Module

- Dashboard
- Miscari paleti
- Rapoarte stoc
- Validari minime
- Repository layer pentru persistenta PostgreSQL
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
- sursa/destinatia sunt obligatorii in functie de tipul miscarii;
- referintele master-data sunt validate in PostgreSQL atunci cand `DATABASE_URL` este configurat.

## Limitari

- fara autentificare;
- fara migratii automate;
- fara conectori reali ERP/WMS/WME;
- fara productie/release/daily-use.
