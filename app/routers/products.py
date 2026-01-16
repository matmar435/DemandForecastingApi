from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SesionLocal
from app.crud.product import get_products, create_product
from app.schemas import ProductResponse, ProductCreate

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


@router.get("/", response_model=list[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.post("/", response_model=list[ProductResponse])
def add_product(
        product: ProductCreate,
        db: Session = Depends(get_db)
):
    return create_product(db,product)


