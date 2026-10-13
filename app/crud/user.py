"""Database operations for User."""
from sqlalchemy.orm import Session
from app.models.user import User

def get_by_email(db: Session, email:str) -> User| None:
    """Return user by email, or None"""
    return db.query(User).filter(User.email == email).first()


def get_by_id(db: Session, user_id: int) -> User | None:
    """Return user by id, or None"""
    return db.get(User,user_id)

def create(db: Session, email:str, hashed_password:str) -> User:
    """create a new user and return it """

    user = User(email=email, hashed_password = hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
