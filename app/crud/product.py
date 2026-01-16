from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas import ProductCreate


def get_products(db: Session):
    return db.query(Product).all()

def create_product(db:Session,product:ProductCreate):
    db_product = Product(
        name=product.name,
        category=product.category
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product