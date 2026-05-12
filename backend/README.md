# Backend - TraceAI Control Paleti

FastAPI MVP skeleton cu fallback demo in-memory si persistence layer PostgreSQL optional.

> MVP skeleton only. No production integrations implemented.

## Rulare locala

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Pentru activarea persistentei PostgreSQL:

```bash
export DATABASE_URL="postgresql+psycopg://traceai:traceai@localhost:5432/traceai_paleti"
```

Fara `DATABASE_URL`, backend-ul ramane in `demo` mode.

## Teste

```bash
pytest
```

## Scope actual

- endpointuri demo/API;
- validari minime;
- repository layer cu fallback demo;
- PostgreSQL optional prin environment variables;
- fara autentificare;
- fara integrare reala ERP/WMS/WME.
