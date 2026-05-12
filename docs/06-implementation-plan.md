# Plan implementare

## Etapa 1 - MVP skeleton

- documentatie initiala;
- backend FastAPI demo;
- frontend React/Vite demo;
- schema SQL;
- teste backend de baza.

## Etapa 2 - Persistenta

- configurare PostgreSQL prin `DATABASE_URL`;
- repository layer cu fallback demo;
- mapare backend la tabelele principale;
- seed controlat pentru dashboard, miscari si raport stoc;
- pending: migratii automate si teste de integrare DB.

## Etapa 3 - Integrare ERP/WMS

- citire parteneri;
- citire stocuri;
- creare/actualizare miscari;
- jurnal sync.

## Etapa 4 - Pilot operational

- inventar initial;
- test receptie/livrare/retur;
- reconciliere.

## Etapa 5 - Extindere WME

- comenzi productie;
- alocare paleti;
- confirmare paletizare.
