from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session
from schemas.user_schema import UserCreate,UserResponse
from service import user_service
from core.db_dependency import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate,db:Session=Depends(get_db)):
    return user_service.add_new_user(user,db)

@router.get("/{user_id}",response_model=UserResponse)
def get_user(user_id:int,db:Session=(Depends(get_db))):
    user = user_service.get_user_by_id(user_id,db)

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user