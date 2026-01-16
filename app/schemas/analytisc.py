from pydantic import BaseModel


class TotalQuantityResponse(BaseModel):
    product_id: int
    total_quantity: int
