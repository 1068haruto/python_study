from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate
from app.crud.user import create_user, delete_user

router = APIRouter()

@router.post("/users/create")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    created_user = create_user(db, user)
    return {"message": "アカウント作成成功！", "user_id": created_user.id}

@router.delete("/users/delete/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    result = delete_user(db, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "アカウント削除成功！"}