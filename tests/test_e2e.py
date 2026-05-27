from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_complete_patient_flow():

    # Register patient
    patient_response = client.post(
        "/register-patient",
        json={
            "firstName": "Sara",
            "lastName": "Ali",
            "age": 25,
            "gender": "Female",
            "department": "Orthopedics"
        }
    )

    assert patient_response.status_code == 200

    patient_id = patient_response.json()["patientId"]

    # Generate token
    token_response = client.post(
        f"/generate-token/{patient_id}"
    )

    assert token_response.status_code == 200
    assert token_response.json()["success"] == True