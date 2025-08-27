from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.auth import hash_password, verify_password


def create_user(db: Session, user: UserCreate):
    # 同名ユーザーが存在するか確認
    existing_user = db.query(User).filter(User.name == user.name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="そのユーザーはすでに存在している")

    # 新規作成
    db_user = User(name=user.name, password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user_data: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    updated = False

    if user_data.name is not None and user_data.name != db_user.name:
        db_user.name = user_data.name
        updated = True
    
    if user_data.password is not None:
        if not verify_password(user_data.password, db_user.password):
            db_user.password = hash_password(user_data.password)
            updated = True
    
    if updated:
        db.commit()
        db.refresh(db_user)
        return {"user_id": db_user.id, "updated": True}
    else:
        return {"user_id": db_user.id, "updated": False}



def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False