# Agent proiect: TraceAI Control - Gestionare Paleti

Acest fisier defineste agentul operational care poate duce proiectul `TraceAI Control - Gestionare Paleti` pana la o versiune pilot stabila, fara a declara prematur productie, release sau daily-use.

## Misiune

Agentul trebuie sa transforme proiectul din MVP skeleton in aplicatie pilot functionala pentru gestiunea paletilor lemn, cu arhitectura clara, teste, documentatie si pasi controlati pentru integrare ERP/WMS/WME.

## Mod de lucru obligatoriu: GitHub/Codex-only

Proiectul NU se lucreaza local. Agentul nu trebuie sa propuna sau sa ceara Terminator, Bash, PowerShell, VS Code local, rulare pe calculatorul utilizatorului sau comenzi locale, decat daca proprietarul proiectului cere explicit acest lucru.

Toate schimbarile se fac direct in GitHub prin:

1. branch dedicat;
2. fisiere create/modificate in branch;
3. PR draft catre `main`;
4. validare prin GitHub Actions;
5. review in PR;
6. merge doar dupa aprobare explicita.

Validarea se face prin GitHub Actions. Daca lipseste un check, agentul trebuie sa adauge sau sa corecteze workflow-ul in GitHub, nu sa mute validarea in local.

## Principii obligatorii

1. Lucreaza doar prin branch + PR.
2. Nu modifica direct `main`.
3. Nu face merge automat.
4. Nu activeaza auto-merge.
5. Nu declara proiectul production-ready.
6. Nu declara release-ready.
7. Nu declara daily-use-ready.
8. Pastreaza fiecare PR narrow si reviewable.
9. Fiecare PR trebuie sa contina scope, non-goals, teste si verdict.
10. Orice integrare ERP/WMS/WME trebuie introdusa initial ca adapter/mock/config, nu ca productie directa.
11. Nu recomanda lucru local decat daca proprietarul proiectului il cere explicit.

## Branch naming

- `codex/docs-*` pentru documentatie.
- `codex/ci-*` pentru CI si calitate.
- `codex/db-*` pentru persistenta si migratii.
- `codex/api-*` pentru backend/API.
- `codex/ui-*` pentru frontend.
- `codex/integration-*` pentru conectori ERP/WMS/WME.
- `codex/pilot-*` pentru pregatire pilot.

## PR body obligatoriu

Fiecare PR trebuie sa includa:

```markdown
## Summary

## Scope

## Non-goals

## Tests

## Risks

## Rollback

## Verdict
```

## Verdicturi acceptate

- `PALETI_DOCS_UPDATED`
- `PALETI_CI_UPDATED`
- `PALETI_DB_PR_CREATED`
- `PALETI_API_PR_CREATED`
- `PALETI_UI_PR_CREATED`
- `PALETI_INTEGRATION_PR_CREATED`
- `PALETI_PILOT_READY_PENDING_APPROVAL`
- `PALETI_BLOCKED`
- `PALETI_FAILED`

## Ordine recomandata de implementare

1. MVP skeleton + CI.
2. Stabilizare teste si structura.
3. Persistenta PostgreSQL.
4. API cu repository/service layer.
5. Frontend conectat la backend.
6. Validari de business extinse.
7. Audit log si sync log.
8. Export rapoarte.
9. Conectori mock ERP/WMS/WME.
10. Conectori reali in mod controlat.
11. Pilot operational.

## Definition of done pentru un PR

Un PR este pregatit pentru review doar daca:

- CI trece;
- documentatia relevanta este actualizata;
- testele acopera comportamentul nou;
- nu introduce integrare productie necontrolata;
- nu modifica scope-ul fara justificare;
- pastreaza explicit non-goals.

## Boundary critic

Pana la aprobarea explicita a proprietarului proiectului:

- fara productie;
- fara release;
- fara daily-use;
- fara conectare la ERP/WMS/WME real;
- fara stocuri reale;
- fara date personale sau comerciale reale;
- fara credentiale in repository;
- fara solutii locale propuse automat.
