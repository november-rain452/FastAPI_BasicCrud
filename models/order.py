from sqlalchemy import Integer, ForeignKey ,Column
from sqlalchemy.orm import relationship
from core.database import Base

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer,primary_key=True)

    user_id = Column(Integer,ForeignKey("users.id"))
    product_id = Column(Integer,ForeignKey("products.id"))

    user = relationship("User",back_populates="orders")
    product = relationship("Product",back_populates="orders")
