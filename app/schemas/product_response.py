from typing import Optional
from pydantic import BaseModel


class ProductResponse(BaseModel):
    name: str
    category: Optional[str]

    class Config:
        orm_mode = True