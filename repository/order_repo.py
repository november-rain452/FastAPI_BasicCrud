from models.order import Order
from sqlalchemy.orm import Session
from schemas.orders_schema import OrderCreate,OrderResponse

def create_order(order:OrderCreate,db:Session):
    order_data = Order(**order.model_dump())
    db.add(order_data)
    db.commit()
    db.refresh(order_data)
    return order_data

def get_order_by_id(order_id:int,db:Session):
    return db.get(Order,order_id)