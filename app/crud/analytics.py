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

def daily_demand_by_product(db:Session,product_id:int):
    results = (
        db.query(
            Order.order_date,
            func.sum(Order.quantity).label("daily_quantity")
        )
        .filter(Order.product_id == product_id)
        .group_by(Order.order_date)
        .order_by(Order.order_date)
        .all()
    )

    return [
        {
            "date": order_date,
            "quantity": quantity
        }
        for order_date, quantity in results
    ]