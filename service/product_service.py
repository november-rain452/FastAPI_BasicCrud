from repository import product_repo
from sqlalchemy.orm import Session
from schemas.product_schema import ProductCreate

def create_product(product :ProductCreate,db:Session):
    return product_repo.create_product(product,db)

def get_product_by_id(product_id:int,db:Session):
    return product_repo.get_product_by_id(product_id,db)