from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models import Order


def total_quantity_by_product(db:Session):
    return (
        db.query(
            Order.product_id,
            func.sum(Order.quantity).label("total_quanticy")
        )
        .group_by(Order.product_id)
        .all()
    )