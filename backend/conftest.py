import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db


# テスト用DBをメモリ上（SQLite）に作成
# MySQLコンテナに依存しないテストをするため
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# get_db の依存関係をオーバーライド
# メモリ内に作成したテスト用DBのセッションを返す
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)  # テスト前にDBを初期化
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)    # テスト後にDBをクリーンアップ


# 事前にユーザーを作成したいテストに使用
@pytest.fixture(scope="function")
def create_test_user(client):
    payload = {"name": "testuser", "password": "testpassword"}
    response = client.post("/users/create", json=payload)
    assert response.status_code == 200
    user_id = response.json()["user_id"]
    return user_id