from repository import order_repo
from sqlalchemy.orm import Session
from schemas.orders_schema import OrderCreate

def create_order(order :OrderCreate,db:Session):
    return order_repo.create_order(order,db)

def get_order_by_id(order_id:int,db:Session):
    return order_repo.get_order_by_id(order_id,db)