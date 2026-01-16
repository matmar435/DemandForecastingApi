from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.analytics import total_quantity_by_product
from app.database import SesionLocal

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/total-quantity")
def total_quantity(db:Session = Depends(get_db)):
    return total_quantity_by_product(db)