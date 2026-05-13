from schemas.product_schema import ProductCreate
from sqlalchemy.orm import Session
from models.product import Product

def create_product(product_data: ProductCreate, db: Session):
    product = Product(**product_data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product_by_id(product_id:int,db:Session):
    product = db.get(Product,product_id)
    return product