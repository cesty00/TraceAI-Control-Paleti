# Pilot readiness checklist

Acest checklist trebuie completat inainte de orice pilot operational.

## Tehnic

- [ ] CI trece pe `main`.
- [ ] Backend are teste pentru fluxurile critice.
- [ ] Frontend build trece.
- [ ] Baza de date este separata de productie.
- [ ] Configuratia este prin environment variables.
- [ ] Nu exista credentiale in repo.

## Date

- [ ] Datele de test sunt sintetice sau aprobate.
- [ ] Nu se folosesc stocuri reale fara aprobare.
- [ ] Nu se folosesc clienti/furnizori reali fara aprobare.
- [ ] Audit log este activ.

## Operare

- [ ] Exista procedura de rollback.
- [ ] Exista responsabil desemnat.
- [ ] Exista interval de test clar.
- [ ] Exista criterii de succes.
- [ ] Exista criterii de oprire.

## Integrare

- [ ] ERP connector ruleaza initial in mod mock/sandbox.
- [ ] WMS connector ruleaza initial in mod mock/sandbox.
- [ ] WME connector ruleaza initial in mod mock/sandbox.
- [ ] Orice write catre sistem real este dezactivat implicit.

## Aprobare

- [ ] Proprietarul proiectului a aprobat pilotul.
- [ ] Scope-ul pilotului este documentat.
- [ ] Verdict: `PALETI_PILOT_READY_PENDING_APPROVAL`.
