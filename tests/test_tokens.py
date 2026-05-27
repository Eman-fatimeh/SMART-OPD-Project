from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_tokens():

    response = client.get("/tokens")

    assert response.status_code == 200
    assert isinstance(response.json(), list)