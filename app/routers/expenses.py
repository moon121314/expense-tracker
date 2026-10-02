from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.database import get_db
from app.models.expense import Expense
from app.models.user import User
from app.schemas.expense import (
    ExpenseCreate,
    ExpenseResponse,
    ExpenseUpdate,
)

router = APIRouter(prefix="/expenses", tags=["expenses"])

DbSession = Annotated[Session, Depends(get_db)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post("/", response_model=ExpenseResponse, status_code=201)
def create_expense(
    expense: ExpenseCreate,
    db: DbSession,
    current_user: CurrentUser,
):
    new_expense = Expense(
        amount=expense.amount,
        category=expense.category,
        user_id=current_user.id,
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


@router.get("/", response_model=list[ExpenseResponse])
def list_expenses(
    db: DbSession,
    current_user: CurrentUser,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
    min_amount: float | None = None,
    category: str | None = None,
):
    query = db.query(Expense).filter(
        Expense.user_id == current_user.id
    )

    if min_amount is not None:
        query = query.filter(Expense.amount >= min_amount)

    if category is not None:
        query = query.filter(Expense.category == category)

    return query.offset(skip).limit(limit).all()


@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(
    expense_id: int,
    db: DbSession,
    current_user: CurrentUser,
):
    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id == current_user.id,
        )
        .first()
    )

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )

    return expense


@router.put("/{expense_id}", response_model=ExpenseResponse)
def update_expense(
    expense_id: int,
    expense: ExpenseUpdate,
    db: DbSession,
    current_user: CurrentUser,
):
    existing_expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id == current_user.id,
        )
        .first()
    )

    if existing_expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )

    updates = expense.model_dump(exclude_unset=True)

    for field, value in updates.items():
        setattr(existing_expense, field, value)

    db.commit()
    db.refresh(existing_expense)

    return existing_expense


@router.delete("/{expense_id}", status_code=204)
def delete_expense(
    expense_id: int,
    db: DbSession,
    current_user: CurrentUser,
):
    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id == current_user.id,
        )
        .first()
    )

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )

    db.delete(expense)
    db.commit()