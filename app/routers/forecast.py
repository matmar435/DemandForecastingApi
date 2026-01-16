from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.analytics import daily_demand_by_product
from app.database import SesionLocal
from app.services.forecast import prepare_dataframe, rolling_mean_forecast

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"]
)


def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{product_id")
def forecast(product_id: int, db: Session = Depends(get_db)):
    data = daily_demand_by_product(db, product_id)

    if len(data) < 7:
        return {"message": "Not enough data to forecast"}

    df = prepare_dataframe(data)
    return rolling_mean_forecast(df)
