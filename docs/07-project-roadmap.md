# Roadmap proiect

## Faza 0 - Design si concept

Status: realizat in Canva si documentatie initiala.

Livrabile:

- prezentare concept;
- arhitectura vizuala;
- scope MVP.

## Faza 1 - MVP skeleton

Obiectiv: aplicatie demonstrativa cu backend, frontend, SQL si CI.

Criterii:

- FastAPI porneste local;
- React/Vite se construieste;
- teste backend trec;
- fara integrari productie.

## Faza 2 - Persistenta PostgreSQL

Obiectiv: inlocuirea datelor in-memory cu repository layer si baza PostgreSQL.

Livrabile:

- conexiune DB configurabila;
- modele/tabele mapate;
- seed controlat;
- teste cu DB de test sau strategy echivalenta.

## Faza 3 - API operational

Obiectiv: endpointuri CRUD si validari reale pentru miscari paleti.

Livrabile:

- creare/listare/validare miscari;
- filtrare miscari;
- rapoarte stoc;
- statusuri sincronizare;
- audit log.

## Faza 4 - UI operational

Obiectiv: frontend conectat la backend.

Livrabile:

- dashboard din API;
- formular miscari din API;
- tabel miscari cu filtre;
- rapoarte vizibile;
- afisare erori validare.

## Faza 5 - Integrari mock ERP/WMS/WME

Obiectiv: contracte si adaptoare mock pentru sisteme externe.

Livrabile:

- interfete connector;
- mock ERP;
- mock WMS;
- mock WME;
- teste pentru fluxuri end-to-end fara sisteme reale.

## Faza 6 - Pilot controlat

Obiectiv: pregatire pentru test operational cu date controlate.

Conditii obligatorii:

- aprobare explicita;
- configuratie separata;
- fara credentiale in repo;
- rollback documentat;
- log si audit validate.
