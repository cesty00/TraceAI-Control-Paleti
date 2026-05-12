# Database schema

Schema PostgreSQL se afla in `database/schema.sql`.

Tabele principale:

- `pallet_items` - articole paleti;
- `locations` - gestiuni si locatii ERP/WMS/WME;
- `partners` - clienti si furnizori;
- `pallet_movements` - miscari paleti;
- `pallet_stock_snapshot` - snapshot stoc;
- `sync_log` - jurnal sincronizare;
- `audit_log` - jurnal audit.

MVP-ul nu foloseste inca baza de date in runtime.

Nota DB persistence: branch-ul de persistenta pastreaza modul demo ca fallback cand `database_url` nu este configurat. CI revalidation trigger.
