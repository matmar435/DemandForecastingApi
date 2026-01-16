from typing import Optional
from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    category: Optional[str] = None