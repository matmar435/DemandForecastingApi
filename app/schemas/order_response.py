from datetime import date
from pydantic import BaseModel


class OrderResponse(BaseModel):
    product_id: int
    order_date: date
    quantity: int
    price: float

    class Config:
        orm_mode = True