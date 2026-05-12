# Backlog agent

Acest backlog este lista de lucru recomandata pentru agentul de proiect.

## EPIC 1 - Stabilizare MVP

- Verifica CI pentru PR initial.
- Corecteaza eventuale erori backend/frontend.
- Adauga reguli de PR si checklist.
- Pregateste merge doar dupa aprobare.

## EPIC 2 - Persistenta PostgreSQL

- [x] Adauga configuratie DB prin environment variables.
- [x] Adauga layer repository.
- [ ] Adauga migratii sau scripturi controlate.
- [x] Inlocuieste demo data in-memory cu DB optional.
- [x] Pastreaza fallback demo daca DB nu este configurata.

## EPIC 3 - Backend API extins

- Filtrare miscari dupa status, tip, palet, partener si document.
- Endpointuri pentru solduri parteneri.
- Endpointuri pentru audit log.
- Endpointuri pentru sync log.
- Validari pe tip de miscare.

## EPIC 4 - Frontend conectat la API

- Dashboard fetch din backend.
- Miscari fetch si create prin backend.
- Validare vizibila in formular.
- Pagina rapoarte conectata la API.
- UI pentru erori si loading state.

## EPIC 5 - Integrari mock

- ERP mock adapter.
- WMS mock adapter.
- WME mock adapter.
- Contracte JSON pentru integrare.
- Teste end-to-end simulate.

## EPIC 6 - Pregatire pilot

- Configuratie separata pilot.
- Ghid de operare.
- Ghid rollback.
- Raport de reconciliere.
- Checklist aprobare pilot.

## Regula de selectie task

Agentul trebuie sa aleaga urmatorul task in ordinea:

1. build/test failure;
2. risc de date sau securitate;
3. blocaj arhitectural;
4. persistenta si API;
5. UI;
6. integrari mock;
7. integrari reale doar cu aprobare explicita.
