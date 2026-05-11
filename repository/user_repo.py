from sqlalchemy.orm import Session
from models.user import User

def create_user(user_data,db):
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user