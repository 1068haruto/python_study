from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.models.user import User
from app.crud.user import create_user, update_user, delete_user


router = APIRouter()


# 作成実行時
@router.post("/users/create")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    created_user = create_user(db, user)
    return {"message": "作成成功！", "user_id": created_user.id}


# 一覧表示時
@router.get("/users/list", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# 更新実行時
@router.put("/users/update/{user_id}")
def update_user_endpoint(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "更新成功！", "user_id": updated_user.id}


# 削除実行時
@router.delete("/users/delete/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    success = delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "削除成功！", "user_id": user_id}