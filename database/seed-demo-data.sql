INSERT INTO pallet_items (pallet_code, name, pallet_type) VALUES
  ('PAL-EUR-1200x800', 'Palet EUR lemn 1200x800', 'EUR'),
  ('PAL-NON-STD', 'Palet lemn nestandard', 'NON_STANDARD'),
  ('PAL-DETERIORAT', 'Palet lemn deteriorat', 'DAMAGED');

INSERT INTO locations (location_code, name, system_owner, location_type) VALUES
  ('WMS_PALETI_BUNI', 'WMS - Paleti buni', 'WMS', 'GOOD'),
  ('WMS_PALETI_DETERIORATI', 'WMS - Paleti deteriorati', 'WMS', 'DAMAGED'),
  ('WME_LINIE_AMBALARE', 'WME - Linie ambalare', 'WME', 'PRODUCTION'),
  ('ERP_SOLD_CLIENTI', 'ERP - Sold clienti', 'ERP', 'CUSTOMER_BALANCE');

INSERT INTO partners (partner_code, name, partner_type, erp_partner_id) VALUES
  ('CUST-ABC', 'Client ABC', 'CUSTOMER', 'ERP-CUST-ABC'),
  ('SUP-LEMN-NORD', 'Furnizor Lemn Nord', 'SUPPLIER', 'ERP-SUP-LEMN-NORD');

INSERT INTO pallet_movements (
  movement_no, movement_type, pallet_item_id, quantity, source_location_id, target_location_id,
  partner_id, reference_document, reference_system, status, created_by
)
SELECT
  'PAL-MOV-0001', 'RECEPTION', p.id, 64, NULL, l.id, s.id, 'REC-2026-0001', 'ERP', 'SYNCED', 'demo'
FROM pallet_items p, locations l, partners s
WHERE p.pallet_code = 'PAL-EUR-1200x800'
  AND l.location_code = 'WMS_PALETI_BUNI'
  AND s.partner_code = 'SUP-LEMN-NORD';

INSERT INTO pallet_stock_snapshot (pallet_item_id, location_id, quantity, source_system)
SELECT p.id, l.id, 842, 'WMS'
FROM pallet_items p, locations l
WHERE p.pallet_code = 'PAL-EUR-1200x800'
  AND l.location_code = 'WMS_PALETI_BUNI';
