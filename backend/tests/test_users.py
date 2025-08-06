from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_create_user():
    response = client.post("/users/create", json={
        "name": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "作成成功！"
    assert "user_id" in response.json()


def test_read_users():
    response = client.get("/users/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # レスポンスボディがリスト型であることを確認


def test_update_user():
    # 前処理: 更新対象のユーザー作成
    create_response = client.post("/users/create", json={
        "name": "user_to_be_updated",
        "password": "testpassword"
    })
    assert create_response.status_code == 200
    created_user_id = create_response.json()["user_id"]
    
    # 本処理
    response = client.put(f"/users/update/{created_user_id}", json={
        "name": "updated_user",
        "password": "updated_password"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "更新成功！"


# ユーザー削除（DELETE）
def test_delete_user():
    # 前処理: 削除対象のユーザー作成
    create_response = client.post("/users/create", json={
        "name": "user_to_be_deleted",
        "password": "testpassword"
    })
    assert create_response.status_code == 200
    created_user_id = create_response.json()["user_id"]

    # 本処理
    response = client.delete(f"/users/delete/{created_user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "削除成功！"