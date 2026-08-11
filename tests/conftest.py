import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.connection import get_connection

@pytest.fixture 
def client():
    return TestClient(app)

# to crate user
@pytest.fixture
def test_user(client):
    unique_id = uuid.uuid4().hex[:8]

    user = {
        "username": f"testuser{unique_id}",
        "email": f"testuser{unique_id}@example.com",
        "password": "Test@1234"
    }

    registration_response = client.post("/auth/registration",
        json=user
    )
    assert registration_response.status_code == 200

    login_response = client.post("/auth/login", json ={
        "email": user["email"],
        "password": user["password"]
    })
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    return {
        "user": user,
        "token": token,
        "headers": {
            "Authorization": f"Bearer {token}"
        }
    }