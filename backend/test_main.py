from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login():
    response = client.post("/login", json={
        "username": "admin",
        "password": "12345@",
        "role": "admin"
    })
    assert response.status_code == 200


def test_get_patients():
    response = client.get("/patients")
    assert response.status_code == 200


def test_get_doctors():
    response = client.get("/doctors")
    assert response.status_code == 200


def test_tokens():
    response = client.get("/tokens")
    assert response.status_code == 200