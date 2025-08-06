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


def test_update_user(create_test_user):
    created_user_id = create_test_user

    response = client.put(f"/users/update/{created_user_id}", json={
        "name": "updated_user",
        "password": "updated_password"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "更新成功！"


def test_delete_user(create_test_user):
    created_user_id = create_test_user

    response = client.delete(f"/users/delete/{created_user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "削除成功！"