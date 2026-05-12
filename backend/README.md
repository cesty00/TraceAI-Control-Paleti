# Backend - TraceAI Control Paleti

FastAPI MVP skeleton cu date demo in-memory.

> MVP skeleton only. No production integrations implemented.

## Rulare locala

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Teste

```bash
pytest
```

## Scope actual

- endpointuri demo;
- validari minime;
- fara baza de date;
- fara autentificare;
- fara integrare reala ERP/WMS/WME.
