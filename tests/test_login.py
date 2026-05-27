from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_admin_login():

    response = client.post(
        "/login",
        json={
            "username": "admin",
            "password": "12345@",
            "role": "admin"
        }
    )

    assert response.status_code == 200
    assert response.json()["success"] == True