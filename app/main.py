from fastapi import FastAPI

from app.database import Base, engine
from app.routers import products, orders, analytics, forecast

app = FastAPI(title="Demand Forecast API")

Base.metadata.create_all(bind=engine)

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(analytics.router)
app.include_router(forecast.router)
