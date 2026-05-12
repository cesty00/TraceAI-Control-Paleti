# Fluxuri integrare ERP/WMS/WME

## Receptie paleti

ERP emite documentul de receptie, TraceAI valideaza codul si cantitatea, iar WMS primeste intrarea in gestiune.

## Alocare productie

WMS furnizeaza stocul disponibil, TraceAI valideaza comanda, iar WME primeste alocarea pe linie.

## Livrare client

WMS confirma incarcarea, TraceAI actualizeaza miscarea, iar ERP tine soldul clientului.

## Retur client

TraceAI inregistreaza returul, separa paletii buni de deteriorati si pregateste actualizarea ERP/WMS.

## Deteriorare si casare

Paletii deteriorati sunt mutati intr-o gestiune blocata; casarea necesita document ERP.

## Reconciliere

Rapoartele compara soldurile ERP, stocurile WMS si confirmarile WME.

> Aceste fluxuri sunt documentate pentru etapa urmatoare. Nu exista sincronizare reala in MVP skeleton.
