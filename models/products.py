from sqlalchemy import Integer,Column,String
from core.database import Base

class Products(Base):

    __tablename__ = "products"

    product_id= Column(Integer,primary_key=True)
    product_name= Column(String,unique=True)
    description = Column(String,unique=True)
    price = Column(Integer)

