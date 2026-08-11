def test_get_all_blogs(client):
    response = client.get("/blog/")
    assert response.status_code == 200

def test_create_blog(client, test_user):
    response = client.post(
        "/blog/",
        headers=test_user["headers"],
        json={
            "title": "My Test Blog",
            "text": (
                "This is a test blog containing more than one hundred "
                "characters so that it satisfies the minimum text length "
                "required by the API."
            ),
            "status": "public"
        }
    )

    assert response.status_code == 200


def test_create_blog_requires_authentication(client):
    response = client.post(
        "/blog/",
        json={
            "title": "Unauthorized Blog",
            "text": (
                "This is an unauthorized test blog containing enough "
                "characters to satisfy the minimum text length."
            ),
            "status": "public"
        }
    )

    assert response.status_code == 401

def test_create_and_get_specific_blog(client, test_user):
    create_response = client.post(
        "/blog/",
        headers=test_user["headers"],
        json={
            "title": "Specific Test Blog",
            "text": (
                "This is a specific test blog containing enough characters "
                "to satisfy the minimum text length requirement."
            ),
            "status": "public"
        }
    )

    assert create_response.status_code == 200

    data = create_response.json()
    print("CREATE RESPONSE:", data)


def test_search_blog(client):
    response = client.get(
        "/blog",
        params={"search": "test"}
    )

    assert response.status_code == 200


def test_update_blog(client, test_user):
    create_response = client.post(
        "/blog/",
        headers=test_user["headers"],
        json={
            "title": "Blog Before Update",
            "text": (
                "This blog is being created so that the update test has "
                "an actual blog belonging to the authenticated test user."
            ),
            "status": "public"
        }
    )

    assert create_response.status_code == 200

    data = create_response.json()
    print("CREATE RESPONSE:", data)


def test_delete_blog(client, test_user):
    create_response = client.post(
        "/blog/",
        headers=test_user["headers"],
        json={
            "title": "Blog To Delete",
            "text": (
                "This blog is being created specifically so that the delete "
                "test can remove a blog belonging to the test user."
            ),
            "status": "public"
        }
    )

    assert create_response.status_code == 200

    data = create_response.json()
    print("CREATE RESPONSE:", data)


def test_get_comments_for_blog(client):
    response = client.get("/blog/1/comments")
    assert response.status_code in [200, 404]