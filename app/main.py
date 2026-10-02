from fastapi import FastAPI

from app.routers import auth, expenses

app = FastAPI(title="Expense Tracker API", version="1.0.0")
app.include_router(expenses.router)
app.include_router(auth.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
