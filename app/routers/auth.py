"""Authentication endpoints."""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import Token, UserCreate, UserResponse
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])

DbSession = Annotated[Session, Depends(get_db)]


@router.post("/register", response_model=UserResponse, status_code=201)
def register(user_in: UserCreate, db: DbSession):
    """Register a new user."""
    return auth_service.register_user(db, user_in)


@router.post("/login", response_model=Token)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: DbSession,
):
    """Authenticate and return a JWT."""
    user = auth_service.authenticate_user(db, form_data.username, form_data.password)
    token = auth_service.create_token_for_user(user)
    return {"access_token": token, "token_type": "bearer"}