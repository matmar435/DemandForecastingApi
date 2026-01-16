from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/demand_forecast"

engine = create_engine(DATABASE_URL)
SesionLocal = sessionmaker(bind=engine)

Base = declarative_base()