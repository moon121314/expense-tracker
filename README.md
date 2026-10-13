# 💰 Expense Tracker API

A production-style REST API for personal expense management, built with **FastAPI, PostgreSQL, and JWT authentication**. Features secure user-level data isolation, automated testing, Docker containerization, and cloud deployment.

**[Live Demo](https://expense-tracker-adds.onrender.com/docs)** · **[GitHub Repository](https://github.com/moon121314/expense-tracker)**

![CI](https://github.com/moon121314/expense-tracker/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1)
![Coverage](https://img.shields.io/badge/Coverage-91%25-brightgreen)

## ✨ Key Features

- **Authentication & Security:** User registration, login, JWT authentication, and bcrypt password hashing using `pwdlib`.
- **Expense Management:** Full CRUD operations with category and minimum-amount filtering.
- **Data Isolation:** Users can access and manage only their own expenses.
- **Database:** PostgreSQL with SQLAlchemy ORM and Alembic migrations.
- **Validation:** Pydantic request and response schemas with centralized configuration.
- **Testing & Code Quality:** 11 pytest tests, 91% test coverage, and Ruff linting.
- **DevOps & Deployment:** Docker, Docker Compose, GitHub Actions CI, Render hosting, and Neon PostgreSQL.

## 🏗️ Architecture

```text
Client
  ↓
FastAPI Routers
  ↓
Services (Business Logic)
  ↓
CRUD (Database Operations)
  ↓
SQLAlchemy ORM
  ↓
PostgreSQL
```

The layered architecture separates HTTP handling, business logic, and database operations to improve maintainability and testability.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Language & Framework | Python 3.12, FastAPI |
| Database & ORM | PostgreSQL 16, SQLAlchemy 2.x |
| Authentication | JWT, python-jose, pwdlib |
| Validation & Config | Pydantic, pydantic-settings |
| Migrations | Alembic |
| Testing & Linting | pytest, TestClient, Ruff |
| DevOps | Docker, GitHub Actions |
| Deployment | Render, Neon |

## 🚀 Run Locally

```bash
git clone https://github.com/moon121314/expense-tracker.git
cd expense-tracker

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

Configure your environment variables and PostgreSQL connection in `.env`, then run:

```bash
uvicorn app.main:app --reload
```

Open **http://127.0.0.1:8000/docs** to explore the interactive API documentation.

## 📊 Project Highlights

- 91% test coverage
- Automated CI checks on every push
- JWT-protected endpoints and user-scoped database queries
- Database schema versioning with Alembic
- Live cloud deployment with interactive API documentation
