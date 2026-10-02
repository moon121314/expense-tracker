# 💰 Expense Tracker API

![CI](https://github.com/moon121314/expense-tracker/actions/workflows/ci.yml/badge.svg)

A production-style **Expense Tracker REST API** built with **FastAPI, PostgreSQL, SQLAlchemy, Alembic, JWT authentication, Docker, and pytest**.

The API allows users to register, authenticate securely, and manage their personal expenses through protected REST endpoints.

---

## 🚀 Features

- 🔐 User registration and authentication
- 🔑 JWT-based authentication
- 🔒 Password hashing
- 👤 User-specific expense data
- 💰 Create, read, update, and delete expenses
- 🔎 Filter expenses by category and minimum amount
- ✅ Request validation with Pydantic
- 🗄️ PostgreSQL database
- 🧩 SQLAlchemy ORM
- 🔄 Alembic database migrations
- 🧪 Automated testing with pytest
- 🧰 FastAPI TestClient
- 🐳 Docker and Docker Compose support
- ⚙️ GitHub Actions CI
- 📚 Interactive Swagger API documentation
- 🛡️ Protected API endpoints

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Alembic | Database migrations |
| Pydantic | Data validation |
| JWT | Authentication |
| pytest | Testing |
| Docker | Containerization |
| GitHub Actions | Continuous Integration |
| Uvicorn | ASGI server |

---

## 📁 Project Structure

```text
expense-tracker/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── auth.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── expense.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── expense.py
│   │   └── token.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       └── expenses.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_expenses.py
│
├── .dockerignore
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── dockerfile
├── requirements.txt
└── README.md
