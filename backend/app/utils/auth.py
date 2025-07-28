from passlib.context import CryptContext            # CryptContextクラス(ハッシュ化アルゴリズムの設定管理)
from datetime import datetime, timedelta, timezone  # timedelta：時間の単位で期間を表現できる
from jose import jwt


SECRET_KEY = "your-dev-secret-key"  # 開発用途
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# インスタンス生成(bcrypt方式使用、新アルゴリズム対応)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# JWT形式のアクセストークン生成
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)