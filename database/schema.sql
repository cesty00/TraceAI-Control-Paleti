CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE pallet_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  pallet_code VARCHAR(50) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  unit VARCHAR(20) NOT NULL DEFAULT 'buc',
  pallet_type VARCHAR(50),
  is_reusable BOOLEAN NOT NULL DEFAULT TRUE,
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE locations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  location_code VARCHAR(80) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  system_owner VARCHAR(20) NOT NULL CHECK (system_owner IN ('ERP','WMS','WME','INTERNAL')),
  location_type VARCHAR(50) NOT NULL,
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE partners (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  partner_code VARCHAR(80) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  partner_type VARCHAR(20) NOT NULL CHECK (partner_type IN ('CUSTOMER','SUPPLIER')),
  erp_partner_id VARCHAR(100),
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE pallet_movements (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  movement_no VARCHAR(80) UNIQUE NOT NULL,
  movement_type VARCHAR(50) NOT NULL,
  pallet_item_id UUID NOT NULL REFERENCES pallet_items(id),
  quantity NUMERIC(12,3) NOT NULL CHECK (quantity > 0),
  source_location_id UUID REFERENCES locations(id),
  target_location_id UUID REFERENCES locations(id),
  partner_id UUID REFERENCES partners(id),
  production_order VARCHAR(100),
  reference_document VARCHAR(100),
  reference_system VARCHAR(20),
  status VARCHAR(30) NOT NULL DEFAULT 'DRAFT',
  error_message TEXT,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_by VARCHAR(100),
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE pallet_stock_snapshot (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  pallet_item_id UUID NOT NULL REFERENCES pallet_items(id),
  location_id UUID NOT NULL REFERENCES locations(id),
  quantity NUMERIC(12,3) NOT NULL,
  source_system VARCHAR(20) NOT NULL,
  snapshot_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE sync_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  movement_id UUID REFERENCES pallet_movements(id),
  target_system VARCHAR(20) NOT NULL,
  request_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  response_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  sync_status VARCHAR(30) NOT NULL,
  error_message TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE audit_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_type VARCHAR(50) NOT NULL,
  entity_id UUID,
  action VARCHAR(50) NOT NULL,
  old_value JSONB,
  new_value JSONB,
  performed_by VARCHAR(100),
  performed_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_pallet_movements_type ON pallet_movements(movement_type);
CREATE INDEX idx_pallet_movements_status ON pallet_movements(status);
CREATE INDEX idx_pallet_movements_reference ON pallet_movements(reference_document);
CREATE INDEX idx_sync_log_status ON sync_log(sync_status);
