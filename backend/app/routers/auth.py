from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.auth import LoginRequest
from app.utils.auth import verify_password, create_access_token, get_current_user


router = APIRouter()


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == request.name).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="認証失敗。")

    access_token = create_access_token(data={"sub": str(user.id)})

    # Cookieにトークンを保存
    response = JSONResponse(content={"message": "ログイン成功！"})
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  # ローカル環境なので False
        samesite="Lax"
    )
    return response


@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name
    }