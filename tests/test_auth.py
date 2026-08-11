
def test_registration(client):
    import uuid
    unique_id = uuid.uuid4().hex[:8]

    response = client.post("/auth/registration",
        json={
            "username": f"newuser{unique_id}",
            "email": f"newuser{unique_id}@example.com",
            "password": "Test@1234"
        }
    )
    assert response.status_code == 200


def test_login(client, test_user):
    response = client.post("/auth/login",
        json={
            "email": test_user["user"]["email"],
            "password": test_user["user"]["password"]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

def test_profile_authenticated(client, test_user):
    response = client.get(
        "/profile/",
        headers=test_user["headers"]
    )
    assert response.status_code == 200


def test_invalid_login(client, test_user):
    response = client.post(
        "/auth/login",
        json={
            "email": test_user["user"]["email"],
            "password": "WrongPassword123!"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Invalid credentials"
