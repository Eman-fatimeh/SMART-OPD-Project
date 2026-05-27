from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_patient():

    response = client.post(
        "/register-patient",
        json={
            "firstName": "Ali",
            "lastName": "Khan",
            "age": 22,
            "gender": "Male",
            "department": "Cardiology"
        }
    )

    assert response.status_code == 200
    assert response.json()["success"] == True