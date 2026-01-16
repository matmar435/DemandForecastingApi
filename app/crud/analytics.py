from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models import Order


def total_quantity_by_product(db: Session):
    results = (
        db.query(
            Order.product_id,
            func.sum(Order.quantity).label("total_quanticy")
        )
        .group_by(Order.product_id)
        .all()
    )

    return [
        {
            "product_id": Order.product_id,
            "total_quantity": total_quantity
        }
        for Order.product_id, total_quantity in results
    ]
