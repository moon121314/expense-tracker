import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = os.getenv("DATABASE_URL",
    "postgresql://moon:moon123@localhost:5432/learning_db",)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    """Yield a database session for a request."""
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()