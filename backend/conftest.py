import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


@pytest.fixture(scope="function")
def create_test_user():
    payload = {"name": "testuser", "password": "testpassword"}
    response = client.post("/users/create", json=payload)
    assert response.status_code == 200
    user_id = response.json()["user_id"]
    return user_id