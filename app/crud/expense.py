"""Database operations for Expense"""
from sqlalchemy.orm import Session
from app.models.expense import Expense

def get_by_id(db: Session, expense_id:int)-> Expense | None:
    """return expense by id, or None"""

    return db.get(Expense,expense_id)

def list_for_user(db: Session, user_id: int, skip: int = 0, limit: int = 10, min_amount: float | None = None, category: str | None = None,) ->list[Expense]:
    """list expense for a specific user with filters,"""
    query = db.query(Expense).filter(Expense.user_id == user_id)

    if min_amount is not None:
        query = query.filter(Expense.amount >= min_amount)
    if category is not None:
        query = query.filter(Expense.category == category)
    return query.order_by(Expense.id).offset(skip).limit(limit).all()

def create(db: Session, user_id: int, amount: float, category: str) -> Expense:
    """Create a new expense and return it"""
    expense = Expense(user_id = user_id, amount = amount, category = category)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def update(db: Session, expense:Expense, updates:dict) -> Expense:
    """Apply updates to an expense and return it"""
    for field, value in updates.items():
        setattr(expense,field,value)

    db.commit()
    db.refresh(expense)
    return expense

def delete(db: Session, expense:Expense) -> None:
    """Delete an expense"""
    db.delete(expense)
    db.commit()
    
        
