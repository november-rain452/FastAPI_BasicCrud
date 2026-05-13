from fastapi import APIRouter,Depends,HTTPException
from schemas.product_schema import ProductCreate,ProductResponse
from sqlalchemy.orm import Session
from core.db_dependency import get_db
from service import product_service


router = APIRouter(prefix="/products",tags=["Product"])

@router.post("/",response_model=ProductResponse)
def add_product(product: ProductCreate,db:Session=(Depends(get_db))):
    return product_service.create_product(product,db)

@router.get("/{product_id}",response_model=ProductResponse)
def get_product(product_id:int,db:Session=(Depends(get_db))):
    product = product_service.get_product_by_id(product_id,db)

    if not product:
        raise HTTPException(status_code=404,detail="Product not found")
    
    return product

