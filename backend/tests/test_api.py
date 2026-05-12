from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["production_integrations_enabled"] is False


def test_dashboard():
    response = client.get("/api/dashboard")
    assert response.status_code == 200
    assert "good_pallets" in response.json()


def test_list_pallet_movements():
    response = client.get("/api/pallet-movements")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_pallet_movement_valid_payload():
    payload = {
        "movement_type": "RECEPTION",
        "pallet_code": "PAL-EUR-1200x800",
        "quantity": 10,
        "target_location": "WMS_PALETI_BUNI",
        "partner_code": "SUP-LEMN-NORD",
        "reference_document": "REC-TEST-001",
        "reference_system": "ERP",
    }
    response = client.post("/api/pallet-movements", json=payload)
    assert response.status_code == 201
    assert response.json()["status"] == "VALIDATED"


def test_create_pallet_movement_invalid_quantity():
    payload = {
        "movement_type": "RECEPTION",
        "pallet_code": "PAL-EUR-1200x800",
        "quantity": 0,
        "target_location": "WMS_PALETI_BUNI",
    }
    response = client.post("/api/pallet-movements", json=payload)
    assert response.status_code == 422


def test_validate_existing_movement():
    response = client.post("/api/pallet-movements/PAL-MOV-0001/validate")
    assert response.status_code == 200
    assert response.json()["valid"] is True


def test_stock_report():
    response = client.get("/api/reports/stock")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
