from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_data: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        # 入力値のみ更新
        if user_data.name is not None and user_data.name != "":
            db_user.name = user_data.name
        if user_data.password is not None and user_data.password != "":
            db_user.password = user_data.password
        db.commit()
        return db_user
    return None

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False