from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_doctor():

    response = client.post(
        "/add-doctor",
        json={
            "name": "Dr Ahmed",
            "specialization": "Cardiologist",
            "department": "Cardiology",
            "status": "Available",
            "schedule": "9AM - 5PM"
        }
    )

    assert response.status_code == 200
    assert response.json()["success"] == True