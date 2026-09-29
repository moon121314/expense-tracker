from fastapi import APIRouter, HTTPException,Query
from app.schemas.expense import ExpenseCreate, ExpenseResponse,ExpenseUpdate
from app.database import get_db

router = APIRouter(prefix="/expenses", tags=["expenses"])


#create post/expense

@router.post("/", response_model=ExpenseResponse, status_code=201)
def create_expense(expense: ExpenseCreate):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("""INSERT INTO expenses(amount,category)
        VALUES (%s,%s)
        RETURNING id, amount,category""",
        (expense.amount,expense.category)
        )
        row = cur.fetchone()
        conn.commit()
    finally:
        cur.close()
        conn.close()

    return {"id": row[0],"amount": float(row[1]), "category": row[2]}

#READ GET/EXPENSE
@router.get("/", response_model=list[ExpenseResponse])
def list_expense(
    skip: int = Query(0,ge=0),
    limit: int = Query(10, ge=1, le=100),
    min_amount: float | None = None,
    category: str | None = None,
):
    conn = get_db()
    cur = conn.cursor()

    query = "SELECT id, amount,category FROM expenses WHERE 1=1"
    params: list = []

    if min_amount is not None:
        query+= " AND amount >= %s"
        params.append(min_amount)

    if category is not None:
        query += " AND category = %s"
        params.append(category)

    query += " ORDER BY id LIMIT %s OFFSET %s"
    params.extend([limit,skip])

    try:

        cur.execute(query,tuple(params))
        rows = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    return [
        {"id":r[0],"amount":float(r[1]),"category":r[2]}
        for r in rows
    ]

#read (one) get/expense/{id}
@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT id, amount, category FROM expenses WHERE id = %s",
            (expense_id,),
        )

        row = cur.fetchone()

    finally:
        cur.close()
        conn.close()


    if row is None:
        raise HTTPException(status_code=404,detail="Expense not found")
    return {"id": row[0],"amount":float(row[1]),"category":row[2]}
    
#update _ put

@router.put("/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, expense: ExpenseUpdate):
    conn = get_db()
    cur = conn.cursor()

    updates = expense.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")

    set_clauses = []
    params: list = []

    for field,value in updates.items():
        set_clauses.append(f"{field} = %s")
        params.append(value)


    params.append(expense_id)

    query =f""" UPDATE expenses SET {', '.join(set_clauses)}
    WHERE id = %s 
    RETURNING id, amount, category """

    try:
        cur.execute(query,tuple(params))
        row = cur.fetchone()
        conn.commit()

    finally:
        cur.close()
        conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return{"id": row[0],"amount": float(row[1]),"category": row[2]}

#delete - delete

@router.delete("/{expense_id}", status_code=204)
def delete_expense(expense_id: int):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
        deleted = cur.rowcount
        conn.commit()

    finally:
        cur.close()
        conn.close()

    if deleted == 0:
        raise HTTPException(status_code=404, detail="Expense not found")


