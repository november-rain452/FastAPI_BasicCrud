from sqlalchemy.orm import Session
from models.user import User
from sqlalchemy import select
from schemas.user_schema import UserCreate

def create_user(user_data:UserCreate,db:Session):
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(user_id,db:Session):
    stmt = select(User).where(User.id==user_id)
    result = db.execute(stmt)
    return result.scalar_one_or_none()