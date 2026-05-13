from fastapi import APIRouter,Depends,HTTPException
from schemas.orders_schema import OrderCreate,OrderResponse
from sqlalchemy.orm import Session
from core.db_dependency import get_db
from service import orders_service

router = APIRouter(prefix="/orders",tags=["Order"])

@router.post("/", response_model=OrderResponse)
def add_order(order:OrderCreate,db:Session = Depends(get_db)):
    return orders_service.create_order(order,db)

@router.get("/{order_id}",response_model=OrderResponse)
def get_single_order(order_id:int,db:Session = Depends(get_db)):
    order = orders_service.get_order_by_id(order_id,db)

    if not order:
        raise HTTPException(status_code=404,detail="Order not found")
    
    return order