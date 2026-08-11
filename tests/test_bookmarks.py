def create_blog(client, test_user):
    response = client.post(
        "/blog/",
        headers=test_user["headers"],
        json={
            "title": "Bookmark Test Blog",
            "text": "This is a test blog with enough text to satisfy the minimum length requirement. This is a test blog with enough text to satisfy the minimum length requirement.",
            "status": "public"
        }
    )

    assert response.status_code == 200
    response = client.get(
        "/profile/blogs",
        headers=test_user["headers"]
    )

    assert response.status_code == 200
    return response.json()[-1]["blog_id"]


def test_create_bookmark(client, test_user):
    blog_id = create_blog(client, test_user)
    response = client.post(
        f"/bookmarks/add/{blog_id}",
        headers=test_user["headers"]
    )
    assert response.status_code == 200


def test_delete_bookmark(client, test_user):
    blog_id = create_blog(client, test_user)
    
    # Create bookmark first
    response = client.post(
        f"/bookmarks/add/{blog_id}",
        headers=test_user["headers"]
    )

    assert response.status_code == 200

    # Delete bookmark
    response = client.delete(
        f"/bookmarks/{blog_id}",
        headers=test_user["headers"]
    )

    assert response.status_code == 200


def test_duplicate_bookmark(client, test_user):
    blog_id = create_blog(client, test_user)

    # First bookmark
    response = client.post(
        f"/bookmarks/add/{blog_id}",
        headers=test_user["headers"]
    )

    assert response.status_code == 200

    # Second bookmark
    response = client.post(
        f"/bookmarks/add/{blog_id}",
        headers=test_user["headers"]
    )

    assert response.status_code == 200
    assert "already exists" in response.json()["message"].lower()