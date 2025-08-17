# create
# --------------------------------------------------------
def test_create_user(client):
    response = client.post("/users/create", json={
        "name": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "user_id" in response.json()


# read
# --------------------------------------------------------
def test_read_users(client):
    response = client.get("/users/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # レスポンスボディがリスト型であることを確認


# update
# --------------------------------------------------------
def test_update_user(client, create_test_user):
    created_user_id = create_test_user

    response = client.put(f"/users/update/{created_user_id}", json={
        "name": "updated_user",
        "password": "updated_password"
    })
    assert response.status_code == 200
    assert "user_id" in response.json()


# delete
# --------------------------------------------------------
def test_delete_user(client, create_test_user):
    created_user_id = create_test_user

    response = client.delete(f"/users/delete/{created_user_id}")
    assert response.status_code == 200
    assert "user_id" in response.json()