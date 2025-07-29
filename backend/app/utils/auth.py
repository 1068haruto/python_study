from fastapi import Depends, HTTPException, Cookie  # 依存性注入、HTTP例外
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from passlib.context import CryptContext            # パスワードのハッシュ化アルゴリズム設定の管理
from datetime import datetime, timedelta, timezone  # 日時操作（現在時刻、時間の差、タイムゾーン）
from jose import JWTError, jwt                      # JWTの生成・検証と関連エラー


SECRET_KEY = "your-dev-secret-key"  # 開発用途
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Cookie(None, alias="access_token")  # ← ここを修正
) -> User:
    if token is None:
        raise HTTPException(status_code=401, detail="トークンがない。")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="トークンが不正。")

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="ユーザーが見つからない。")

    return user