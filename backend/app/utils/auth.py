from fastapi import Depends, HTTPException          # 依存性注入、HTTP例外
from fastapi.security import OAuth2PasswordBearer   # OAuth2 (Bearerトークン) 認証スキーム
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from passlib.context import CryptContext            # パスワードのハッシュ化アルゴリズム設定の管理
from datetime import datetime, timedelta, timezone  # 日時操作（現在時刻、時間の差、タイムゾーン）
from jose import JWTError, jwt                      # JWTの生成・検証と関連エラー


# --- 設定 ---
SECRET_KEY = "your-dev-secret-key"  # 開発用途
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# --- パスワードハッシュ化・検証関連 ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# --- JWTアクセストークン関連 ---
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# --- 認証依存性注入関連 ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="認証情報が正しくない",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
    return user