import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app import models  # noqa: F401


TEST_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://moon:moon123@localhost:5432/test_db",
)

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def create_tables():
    """Create tables before each test, drop them after."""
    Base.metadata.create_all(bind=engine)
    yield
    with engine.connect() as conn:
        conn.exec_driver_sql(
            "TRUNCATE expenses, users RESTART IDENTITY CASCADE;"
        )
        conn.commit()


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def registered_user(client):
    payload = {"email": "test@test.com", "password": "mypassword123"}
    client.post("/auth/register", json=payload)
    return payload


@pytest.fixture
def auth_token(client, registered_user):
    resp = client.post(
        "/auth/login",
        data={"username": registered_user["email"], "password": registered_user["password"]},
    )
    return resp.json()["access_token"]


@pytest.fixture
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}