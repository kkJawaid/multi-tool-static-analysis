def test_get_profile(client, test_user):
    response = client.get(
        "/profile/",
        headers=test_user["headers"]
    )

    assert response.status_code == 200
    data = response.json()
    assert data["user_email"] == test_user["user"]["email"]
    assert data["user_name"] == test_user["user"]["username"]


def test_update_profile(client, test_user):
    response = client.patch(
        "/profile/",
        headers=test_user["headers"],
        json={
            "user_name": "updateduser123",
            "user_email": "updateduser123@example.com"
        }
    )
    assert response.status_code == 200


def test_get_user_blogs(client, test_user):
    response = client.get(
        "/profile/blogs",
        headers=test_user["headers"]
    )
    assert response.status_code == 200


def test_get_user_comments(client, test_user):
    response = client.get(
        "/profile/comments",
        headers=test_user["headers"]
    )
    assert response.status_code == 200


def test_get_user_bookmarks(client, test_user):
    response = client.get(
        "/profile/bookmarks",
        headers=test_user["headers"]
    )
    assert response.status_code == 200


def test_profile_endpoints_require_authentication(client):
    endpoints = [
        "/profile/",
        "/profile/blogs",
        "/profile/comments",
        "/profile/bookmarks"
    ]

    for endpoint in endpoints:
        response = client.get(endpoint)

        assert response.status_code == 401