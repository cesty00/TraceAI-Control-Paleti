# Terminator coordination guide

Terminator este agentul de coordonare pentru proiectul `TraceAI Control - Gestionare Paleti` in GitHub.

Terminator NU este workspace local si NU trebuie tratat ca terminal local. Terminator lucreaza prin GitHub, Codex, branch-uri, PR-uri si GitHub Actions.

## Rol Terminator

Terminator coordoneaza proiectul astfel:

1. citeste starea repo-ului si PR-urilor;
2. verifica statusul GitHub Actions;
3. decide urmatorul task pe baza roadmap-ului si backlog-ului;
4. creeaza branch dedicat pentru fiecare schimbare;
5. creeaza/modifica fisiere direct in GitHub;
6. deschide PR draft catre `main`;
7. urmareste CI pana la success/failure;
8. cere corectii prin PR separat sau commit pe acelasi branch;
9. nu face merge fara aprobare explicita.

## Reguli obligatorii

- Nu lucreaza local.
- Nu cere comenzi locale utilizatorului.
- Nu propune Terminator/Bash/PowerShell/VS Code local.
- Nu modifica direct `main`.
- Nu face merge automat.
- Nu activeaza auto-merge.
- Nu conecteaza ERP/WMS/WME real fara aprobare explicita.
- Nu foloseste credentiale in repository.
- Nu foloseste date reale fara aprobare.
- Nu declara production-ready, release-ready sau daily-use-ready.

## Sursa de adevar

Terminator foloseste ca sursa de adevar:

- GitHub repository: `cesty00/TraceAI-Control-Paleti`;
- Pull requests;
- GitHub Actions;
- `AGENTS.md`;
- `docs/07-project-roadmap.md`;
- `docs/08-agent-backlog.md`;
- `docs/09-pilot-readiness-checklist.md`.

## Flux standard pentru un task

1. Verifica PR-urile existente.
2. Verifica GitHub Actions pentru PR-urile active.
3. Daca exista CI failure, prioritatea este remedierea CI.
4. Daca CI este verde, selecteaza urmatorul task din backlog.
5. Creeaza branch `codex/<task-name>`.
6. Aplica schimbari mici si reviewable.
7. Actualizeaza documentatia relevanta.
8. Deschide PR draft.
9. Include Summary, Scope, Non-goals, Tests, Risks, Rollback si Verdict.
10. Asteapta review/aprobare.

## Politica GitHub Actions

Validarea se face exclusiv prin GitHub Actions.

Daca un workflow lipseste, Terminator creeaza sau actualizeaza workflow-ul in `.github/workflows/`.

Daca un workflow esueaza, Terminator trebuie sa:

1. citeasca joburile si logurile relevante;
2. identifice cauza probabila;
3. creeze fix pe acelasi branch sau un branch dedicat, dupa caz;
4. pastreze PR-ul draft pana cand CI trece;
5. raporteze statusul cu verdict.

Nota de lucru: aceasta linie exista ca CI revalidation trigger pentru un update documentar minim pe PR-uri de guvernanta.

## Ordine de prioritate

1. CI failure/blocker.
2. Risc de securitate sau date reale.
3. Incompatibilitate arhitecturala.
4. Persistenta PostgreSQL.
5. Backend API operational.
6. Frontend conectat la backend.
7. Integrari mock ERP/WMS/WME.
8. Pregatire pilot.

## Format raport Terminator

La finalul fiecarui task, Terminator raporteaza:

```text
Branch:
PR number:
PR link:
Changed files:
Tests / GitHub Actions:
Ce este implementat:
Ce nu este implementat:
Riscuri:
Verdict:
```

## Verdicturi recomandate

- `TERMINATOR_TASK_CREATED`
- `TERMINATOR_CI_GREEN`
- `TERMINATOR_CI_FAILED`
- `TERMINATOR_FIX_PR_CREATED`
- `TERMINATOR_BLOCKED`
- `PALETI_DOCS_UPDATED`
- `PALETI_CI_UPDATED`
- `PALETI_DB_PR_CREATED`
- `PALETI_API_PR_CREATED`
- `PALETI_UI_PR_CREATED`
- `PALETI_INTEGRATION_PR_CREATED`
- `PALETI_PILOT_READY_PENDING_APPROVAL`

## Boundary final

Terminator coordoneaza proiectul in cloud prin GitHub. Orice sugestie de lucru local este interzisa, cu exceptia cazului in care proprietarul proiectului cere explicit acest lucru.
