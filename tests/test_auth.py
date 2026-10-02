def test_register_success(client):
    resp = client.post(
        "/auth/register",
        json={"email": "new@test.com", "password": "mypassword123"},
    )
    assert resp.status_code == 201
    assert resp.json()["email"] == "new@test.com"


def test_register_duplicate_email(client, registered_user):
    resp = client.post("/auth/register", json=registered_user)
    assert resp.status_code == 400


def test_login_success(client, registered_user):
    resp = client.post(
        "/auth/login",
        data={
            "username": registered_user["email"],
            "password": registered_user["password"],
        },
    )
    assert resp.status_code == 200
    assert "access_token" in resp.json()


def test_login_wrong_password(client, registered_user):
    resp = client.post(
        "/auth/login",
        data={"username": registered_user["email"], "password": "wrongpass"},
    )
    assert resp.status_code == 401