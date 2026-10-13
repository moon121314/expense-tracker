"""Main FastAPI application."""

from fastapi import FastAPI

from app.core.config import settings
from app.routers import auth, expenses

app = FastAPI(title=settings.app_name, version="1.0.0")
app.include_router(auth.router)
app.include_router(expenses.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
