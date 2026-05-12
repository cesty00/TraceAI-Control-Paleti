# TraceAI Control - Gestionare Paleti

MVP skeleton pentru gestionarea paletilor reutilizabili printr-un strat UI si API intre ERP, WMS si WME.

## Scop

Aplicatia urmareste miscari de paleti lemn intre furnizori, depozit, productie, clienti si retururi. Repository-ul contine un MVP skeleton, date demo, documentatie initiala si un persistence layer PostgreSQL optional pentru etapa pilot.

> MVP skeleton only. No production integrations implemented.

## Structura

- `backend/` - FastAPI skeleton cu fallback demo si persistenta PostgreSQL optionala.
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

Pentru PostgreSQL optional:

```bash
export DATABASE_URL="postgresql+psycopg://traceai:traceai@localhost:5432/traceai_paleti"
```

Cand `DATABASE_URL` lipseste, backend-ul ruleaza in continuare in `demo` mode cu date in-memory.

Endpointuri demo/API:

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
- migratii automate si orchestration DB pentru medii multiple;
- productie/release/daily-use;
- sincronizare reala de documente sau stocuri.
