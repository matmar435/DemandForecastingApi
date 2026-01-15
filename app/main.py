from fastapi import FastAPI

app = FastAPI(title="Demand Forecast API")


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok"}
