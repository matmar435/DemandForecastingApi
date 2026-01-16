from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.order import get_orders, create_order
from app.routers.products import get_db
from app.schemas import OrderResponse, OrderCreate

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.get("/", response_model=list[OrderResponse])
def read_order(db: Session = Depends(get_db)):
    return get_orders(db)

@router.post("/", response_model=list[OrderResponse])
def add_product(
        order: OrderCreate,
        db: Session = Depends(get_db)
):
    return create_order(db,order)