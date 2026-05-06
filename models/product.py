from sqlalchemy import Integer,Column,String,Float
from sqlalchemy.orm import relationship
from core.database import Base

class Product(Base):

    __tablename__ = "products"

    id= Column(Integer,primary_key=True)
    product_name= Column(String,unique=True)
    price = Column(Float)

    orders = relationship("Order",back_populates="product")


