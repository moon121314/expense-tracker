from fastapi import FastAPI

app = FastAPI(
    title="Expense Tracker API",
    description="A simple API for tracking expenses",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    """Return service health status."""
    return {"status": "ok"}