from fastapi import APIRouter, HTTPException
from app.schemas.expense import ExpenseCreate, ExpenseResponse
from app.database import get_db

router = APIRouter(prefix="/expenses", tags=["expenses"])

_expenses: list[dict] = []
_next_id = 1


@router.get("/", response_model=list[ExpenseResponse])
def list_expenses():
    return _expenses


@router.post("/", response_model=ExpenseResponse, status_code=201)
def create_expense(expense: ExpenseCreate):
    global _next_id
    new = {"id": _next_id, **expense.model_dump()}
    _expenses.append(new)
    _next_id += 1
    return new


@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int):
    for e in _expenses:
        if e["id"] == expense_id:
            return e
    raise HTTPException(status_code=404, detail="Expense not found")


@router.delete("/{expense_id}", status_code=204)
def delete_expense(expense_id: int):
    global _expenses
    before = len(_expenses)
    _expenses = [e for e in _expenses if e["id"] != expense_id]
    if len(_expenses) == before:
        raise HTTPException(status_code=404, detail="Expense not found")


@router.get("/db", response_model=list[ExpenseResponse])
def db_expenses():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, amount, category FROM expenses")
        rows = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return [
        {"id": r[0], "amount": float(r[1]), "category": r[2]}
        for r in rows
    ]