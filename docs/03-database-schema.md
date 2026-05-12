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

Runtime-ul backend poate folosi schema atunci cand `DATABASE_URL` este configurat.

In lipsa configuratiei DB, backend-ul pastreaza fallback-ul demo in-memory pentru a nu bloca MVP-ul.

Seed-ul controlat se afla in `database/seed-demo-data.sql` si acopera dashboard, miscari demo si raportul de stoc.
