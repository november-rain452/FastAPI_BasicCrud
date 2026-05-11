from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user_schema import UserCreate,UserResponse
from service import user_service
from core.db_dependency import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/add", response_model=UserCreate)
def create_user(user: UserCreate,db:Session=Depends(get_db)):
    return user_service.add_new_user(user,db)

@router.get("/{user.id}")
def get_user(user_id:int):
    return user_service.get_user_by_id(user_id)