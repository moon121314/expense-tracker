"""Business logic for authentication"""
import logging

from fastapi import HTTPException,status
from sqlalchemy.orm import Session

from app.core.security import hash_password,verify_password,create_access_token
from app.crud import user as user_crud
from app.models.user import User
from app.schemas.user import UserCreate

logger = logging.getLogger(__name__)

def register_user(db: Session, user_in: UserCreate) -> User:
    """Register a new user. fails if email exists"""

    if user_crud.get_by_email(db,user_in.email):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    hashed = hash_password(user_in.password)
    user = user_crud.create(db, user_in.email, hashed)
    logger.info("User registered: %s", user.email)
    return user

def authenticate_user(db: Session, email: str, password: str) -> User:
    """Authenticate a user. Fails if credentials are wrong."""
    user = user_crud.get_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def create_token_for_user(user: User) -> str:
    """Create a JWT for the given user."""
    return create_access_token({"sub": str(user.id)})
