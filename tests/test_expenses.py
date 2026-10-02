def test_create_expense_requires_auth(client):
    resp = client.post("/expenses/", json={"amount": 500, "category": "food"})
    assert resp.status_code == 401


def test_create_expense_success(client, auth_headers):
    resp = client.post(
        "/expenses/",
        json={"amount": 500, "category": "food"},
        headers=auth_headers,
    )
    assert resp.status_code == 201
    assert resp.json()["amount"] == 500


def test_list_expenses(client, auth_headers):
    client.post("/expenses/", json={"amount": 100, "category": "food"}, headers=auth_headers)
    client.post("/expenses/", json={"amount": 200, "category": "transport"}, headers=auth_headers)
    resp = client.get("/expenses/", headers=auth_headers)
    assert resp.status_code == 200
    assert len(resp.json()) == 2


def test_get_expense_not_found(client, auth_headers):
    resp = client.get("/expenses/9999", headers=auth_headers)
    assert resp.status_code == 404


def test_update_expense(client, auth_headers):
    create = client.post(
        "/expenses/",
        json={"amount": 100, "category": "food"},
        headers=auth_headers,
    )
    expense_id = create.json()["id"]
    resp = client.put(
        f"/expenses/{expense_id}",
        json={"amount": 750},
        headers=auth_headers,
    )
    assert resp.status_code == 200
    assert resp.json()["amount"] == 750


def test_delete_expense(client, auth_headers):
    create = client.post(
        "/expenses/",
        json={"amount": 100, "category": "food"},
        headers=auth_headers,
    )
    expense_id = create.json()["id"]
    resp = client.delete(f"/expenses/{expense_id}", headers=auth_headers)
    assert resp.status_code == 204


def test_user_isolation(client):
    # Register user A and user B
    client.post("/auth/register", json={"email": "a@test.com", "password": "pass1234"})
    client.post("/auth/register", json={"email": "b@test.com", "password": "pass1234"})

    token_a = client.post(
        "/auth/login", data={"username": "a@test.com", "password": "pass1234"}
    ).json()["access_token"]
    token_b = client.post(
        "/auth/login", data={"username": "b@test.com", "password": "pass1234"}
    ).json()["access_token"]

    # A creates an expense
    create = client.post(
        "/expenses/",
        json={"amount": 100, "category": "food"},
        headers={"Authorization": f"Bearer {token_a}"},
    )
    expense_id = create.json()["id"]

    # B tries to fetch A's expense → 404
    resp = client.get(
        f"/expenses/{expense_id}",
        headers={"Authorization": f"Bearer {token_b}"},
    )
    assert resp.status_code == 404