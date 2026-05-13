from repository import order_repo
from sqlalchemy.orm import Session

def create_order(order,db:Session):
    return order_repo.create_order(order,db)

def get_order_by_id(order_id,db:Session):
    return order_repo.get_order_by_id(order_id,db)