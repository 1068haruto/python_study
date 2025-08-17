# --------------------------------------------------------
# create
# --------------------------------------------------------
def test_create_user(client):
    """
    適切な入力の場合、作成成功
    """
    response = client.post("/users/create", json={
        "name": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "user_id" in response.json()


def test_create_user_duplicate(client):
    """
    既存ユーザーと同名で登録する場合、作成失敗
    """
    # 1回目（成功）
    client.post("/users/create", json={
        "name": "duplicate_user",
        "password": "password123"
    })

    # 2回目（ユニーク制約により失敗）
    response = client.post("/users/create", json={
        "name": "duplicate_user",
        "password": "password123"
    })
    assert response.status_code in (400, 409)


def test_create_user_empty_name(client):
    """
    ユーザー名が空欄の場合、作成失敗
    """
    response = client.post("/users/create", json={
        "name": "",  # 空のユーザー名
        "password": "testpassword"
    })
    assert response.status_code == 422
    assert "detail" in response.json()


def test_create_user_empty_password(client):
    """
    パスワードが空欄の場合、作成失敗
    """
    response = client.post("/users/create", json={
        "name": "testuser",
        "password": ""  # 空のパスワード
    })
    assert response.status_code == 422
    assert "detail" in response.json()


def test_create_user_empty_name_and_password(client):
    """
    ユーザー名とパスワードが空欄の場合、作成失敗
    """
    response = client.post("/users/create", json={
        "name": "",
        "password": ""
    })
    assert response.status_code == 422
    assert "detail" in response.json()


# --------------------------------------------------------
# read
# --------------------------------------------------------
def test_read_users(client):
    response = client.get("/users/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # レスポンスボディがリスト型であることを確認


# --------------------------------------------------------
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


# --------------------------------------------------------
# delete
# --------------------------------------------------------
def test_delete_user(client, create_test_user):
    created_user_id = create_test_user

    response = client.delete(f"/users/delete/{created_user_id}")
    assert response.status_code == 200
    assert "user_id" in response.json()