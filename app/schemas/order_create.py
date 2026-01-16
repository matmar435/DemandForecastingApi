from datetime import date
from pydantic import BaseModel


class OrderCreate(BaseModel):
    product_id: int
    order_date: date
    quantity: int
    price: float