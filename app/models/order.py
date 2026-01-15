from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from app.database import Base

class Order(Base):
    _tablename_ = "orders"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    order_date = Column(Date)
    quantity = Column(Integer)
    price = Column(Numeric)

    product = relationship("Product", back_populates="orders")