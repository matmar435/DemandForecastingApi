from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.analytics import total_quantity_by_product, daily_demand_by_product
from app.database import SesionLocal
from app.schemas import TotalQuantityResponse

router = APIRouter(prefix="/analytics", tags=["Analytics"])


def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/total-quantity", response_model=list[TotalQuantityResponse])
def total_quantity(db: Session = Depends(get_db)):
    return total_quantity_by_product(db)


@router.get("/daily-demand/{product_id}")
def daily_demand(product_id: int, db: Session = Depends(get_db)):
    return daily_demand_by_product(db, product_id)
