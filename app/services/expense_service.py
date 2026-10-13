"""Business logic for expenses."""

import logging

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.crud import expense as expense_crud
from app.models.expense import Expense
from app.models.user import User
from app.schemas.expense import ExpenseCreate, ExpenseUpdate

logger = logging.getLogger(__name__)


def list_user_expenses(
    db: Session,
    user: User,
    skip: int = 0,
    limit: int = 10,
    min_amount: float | None = None,
    category: str | None = None,
) -> list[Expense]:
    """Return a user's expenses"""

    return expense_crud.list_for_user(
        db,
        user_id=user.id,
        skip=skip,
        limit=limit,
        min_amount=min_amount,
        category=category,
    )


def get_user_expense(db: Session, user: User, expense_id: int) -> Expense:
    """Return an expense belonging to the user, or raise 404."""
    expense = expense_crud.get_by_id(db, expense_id)
    if expense is None or expense.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found"
        )
    return expense


def create_user_expense(db: Session, user: User, expense_in: ExpenseCreate) -> Expense:
    """Create a new expense for the user."""
    expense = expense_crud.create(
        db, user_id=user.id, amount=expense_in.amount, category=expense_in.category
    )
    logger.info("Expense created: id=%s user=%s", expense.id, user.id)
    return expense


def update_user_expense(
    db: Session, user: User, expense_id: int, updates_in: ExpenseUpdate
) -> Expense:
    """Update a user's expense."""
    expense = get_user_expense(db, user, expense_id)

    updates = updates_in.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update",
        )

    return expense_crud.update(db, expense, updates)


def delete_user_expense(db: Session, user: User, expense_id: int) -> None:
    """Delete a user's expense."""
    expense = get_user_expense(db, user, expense_id)
    expense_crud.delete(db, expense)
