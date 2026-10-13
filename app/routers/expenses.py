"""Expense endpoints."""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.database import get_db
from app.models.user import User
from app.schemas.expense import ExpenseCreate, ExpenseResponse, ExpenseUpdate
from app.services import expense_service

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post("/", response_model=ExpenseResponse, status_code=201)
def create_expense(
    expense_in: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new expense for the current user."""
    return expense_service.create_user_expense(db, current_user, expense_in)


@router.get("/", response_model=list[ExpenseResponse])
def list_expenses(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    min_amount: float | None = None,
    category: str | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """List the current user's expenses."""
    return expense_service.list_user_expenses(
        db, current_user, skip, limit, min_amount, category
    )


@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Return a single expense."""
    return expense_service.get_user_expense(db, current_user, expense_id)


@router.put("/{expense_id}", response_model=ExpenseResponse)
def update_expense(
    expense_id: int,
    updates_in: ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update an expense."""
    return expense_service.update_user_expense(db, current_user, expense_id, updates_in)


@router.delete("/{expense_id}", status_code=204)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete an expense."""
    expense_service.delete_user_expense(db, current_user, expense_id)
