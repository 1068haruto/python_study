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
    """
    適切な入力の場合、更新成功
    """
    created_user_id = create_test_user

    # ユーザー名とパスワードを両方更新する場合
    response = client.put(f"/users/update/{created_user_id}", json={
        "name": "updated_user",
        "password": "updated_password"
    })
    assert response.status_code == 200
    assert "user_id" in response.json()

    # ユーザー名のみを更新する場合
    response = client.put(f"/users/update/{created_user_id}", json={
        "name": "updated_user"
    })
    assert response.status_code == 200
    assert "user_id" in response.json()
    
    # パスワードのみを更新する場合
    response = client.put(f"/users/update/{created_user_id}", json={
        "password": "updated_password"
    })
    assert response.status_code == 200
    assert "user_id" in response.json()


def test_update_user_not_found(client):
    """
    存在しないユーザーIDの場合、更新失敗
    """
    response = client.put("/users/update/99999", json={
        "name": "updated_user",
        "password": "updated_password"
    })
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_update_user_invalid_input(client, create_test_user):
    """
    無効な入力（min_length=1に違反）の場合、更新失敗
    """
    created_user_id = create_test_user

    # ユーザー名が空の場合
    response = client.put(f"/users/update/{created_user_id}", json={
        "name": "",
        "password": "updated_password"
    })
    assert response.status_code == 422
    assert "detail" in response.json()
    assert any(err["loc"] == ["body", "name"] for err in response.json()["detail"])

    # パスワードが空の場合
    response = client.put(f"/users/update/{created_user_id}", json={
        "name": "updated_user",
        "password": ""
    })
    assert response.status_code == 422
    assert "detail" in response.json()
    assert any(err["loc"] == ["body", "password"] for err in response.json()["detail"])


# --------------------------------------------------------
# delete
# --------------------------------------------------------
def test_delete_user(client, create_test_user):
    created_user_id = create_test_user

    response = client.delete(f"/users/delete/{created_user_id}")
    assert response.status_code == 200
    assert "user_id" in response.json()