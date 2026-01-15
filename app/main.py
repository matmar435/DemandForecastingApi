from fastapi import FastAPI

from app.database import Base, engine

app = FastAPI(title="Demand Forecast API")

Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return {"status": "API is running"}
