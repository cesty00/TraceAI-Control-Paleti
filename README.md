# TraceAI Control - Gestionare Paleti

MVP skeleton pentru gestionarea paletilor reutilizabili printr-un strat UI si API intre ERP, WMS si WME.

## Scop

Aplicatia urmareste miscari de paleti lemn intre furnizori, depozit, productie, clienti si retururi. Acest repository contine doar un MVP skeleton, date demo si documentatie initiala.

> MVP skeleton only. No production integrations implemented.

## Structura

- `backend/` - FastAPI skeleton cu date in-memory.
- `frontend/` - React/Vite skeleton cu UI demo.
- `database/` - schema PostgreSQL si seed demo.
- `docs/` - documentatie functionala si tehnica MVP.
- `integrations/` - note pentru viitori conectori ERP, WMS si WME.

## Backend local

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Endpointuri demo:

- `GET /health`
- `GET /api/dashboard`
- `GET /api/pallet-movements`
- `POST /api/pallet-movements`
- `POST /api/pallet-movements/{id}/validate`
- `GET /api/reports/stock`

Teste backend:

```bash
cd backend
pytest
```

## Frontend local

```bash
cd frontend
npm install
npm run dev
npm run build
```

## Nu este implementat inca

- integrare reala ERP/WMS/WME;
- autentificare;
- conexiune baza de date;
- productie/release/daily-use;
- sincronizare reala de documente sau stocuri.
