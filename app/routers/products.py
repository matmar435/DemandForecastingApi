from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SesionLocal
from app.crud.product import get_products

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/pro")
def read_products(db: Session = Depends(get_db)):
    return get_products(db)


