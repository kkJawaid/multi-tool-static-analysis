def create_blog(client, test_user):
    response = client.post(
        "/blog/",
        headers=test_user["headers"],
        json={
            "title": "Comment Test Blog",
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


def create_comment(client, test_user, blog_id):
    response = client.post(
        f"/comments/{blog_id}",
        headers=test_user["headers"],
        json={
            "commentText": "This is a test comment."
        }
    )

    assert response.status_code == 200
    response = client.get(f"/blog/{blog_id}/comments")
    assert response.status_code == 200

    return response.json()["comments"][-1]["comment_id"]


def test_create_comment(client, test_user):
    blog_id = create_blog(client, test_user)

    response = client.post(
        f"/comments/{blog_id}",
        headers=test_user["headers"],
        json={
            "commentText": "This is a test comment."
        }
    )

    assert response.status_code == 200


def test_update_comment(client, test_user):
    blog_id = create_blog(client, test_user)
    comment_id = create_comment(client, test_user, blog_id)

    response = client.patch(
        f"/comments/{blog_id}/{comment_id}",
        headers=test_user["headers"],
        json={
            "commentText": "This is the updated comment."
        }
    )

    assert response.status_code == 200


def test_delete_comment(client, test_user):
    blog_id = create_blog(client, test_user)
    comment_id = create_comment(client, test_user, blog_id)

    response = client.delete(
        f"/comments/{blog_id}/{comment_id}",
        headers=test_user["headers"]
    )

    assert response.status_code == 200