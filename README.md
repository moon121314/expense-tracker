# 💰 Expense Tracker API

A production-style REST API for tracking personal expenses, built with **FastAPI**, **PostgreSQL**, and **JWT authentication**. Containerized with **Docker**, tested with **pytest (91% coverage)**, and deployed to the cloud via **GitHub Actions CI**.

![CI](https://github.com/moon121314/expense-tracker/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-✓-blue)
![Coverage](https://img.shields.io/badge/coverage-91%25-brightgreen)

**🔗 Live Demo:** https://expense-tracker-adds.onrender.com/docs

> **Note:** Hosted on Render's free tier. First request after 15 minutes of inactivity may take ~60 seconds to spin up.

---

## 📌 Overview

A backend service for tracking personal expenses. Each user registers, logs in, and manages only their own data — enforced at the query layer. The API is structured in a layered architecture (`routers → services → crud → models`) for maintainability and testability.

---

## ✨ Features

- **User registration and login** with JWT authentication
- **Bcrypt password hashing** via pwdlib
- **User-scoped data isolation** — each user sees only their own expenses
- **Full CRUD** for expenses
- **Filtering** by category and minimum amount
- **Pagination** with `skip` and `limit`
- **Pydantic validation** for all request/response models
- **Layered architecture**: routers → services → crud → models
- **Centralized configuration** with `pydantic-settings`, fail-fast at startup
- **PostgreSQL** with SQLAlchemy ORM
- **Alembic migrations** for schema versioning
- **91% test coverage** with pytest (11 tests)
- **GitHub Actions CI** — runs pytest + Ruff on every push
- **Dockerized** with multi-layer caching
- **Deployed** on Render + Neon

---

## 🏗️ Architecture
┌───────────────┐
│ HTTP Client │
└───────┬───────┘
│
▼
┌───────────────┐
│ Routers │ ← HTTP layer (FastAPI)
└───────┬───────┘
│
▼
┌───────────────┐
│ Services │ ← Business logic
└───────┬───────┘
│
▼
┌───────────────┐
│ CRUD │ ← Database operations
└───────┬───────┘
│
▼
┌───────────────┐
│ SQLAlchemy │
└───────┬───────┘
│
▼
┌───────────────┐
│ PostgreSQL │
└───────────────┘

**Rule:** Never skip layers. Routers call services. Services call CRUD. CRUD talks to the DB.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| Web framework | FastAPI |
| Database | PostgreSQL 16 |
| ORM | SQLAlchemy 2.x |
| Migrations | Alembic |
| Auth | JWT (python-jose) + pwdlib |
| Config | pydantic-settings |
| Validation | Pydantic |
| Testing | pytest, TestClient |
| Linting | Ruff |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Hosting | Render + Neon |

---

## 📁 Project Structure
expense-tracker-api/
│
├── app/
│ ├── main.py FastAPI entry point
│ ├── database.py Engine, SessionLocal, get_db
│ │
│ ├── core/
│ │ ├── config.py pydantic-settings Settings
│ │ ├── security.py JWT + password hashing
│ │ └── deps.py get_current_user, DbSession
│ │
│ ├── models/ SQLAlchemy models
│ │ ├── user.py
│ │ └── expense.py
│ │
│ ├── schemas/ Pydantic schemas
│ │ ├── user.py
│ │ └── expense.py
│ │
│ ├── crud/ Database operations
│ │ ├── user.py
│ │ └── expense.py
│ │
│ ├── services/ Business logic
│ │ ├── auth_service.py
│ │ └── expense_service.py
│ │
│ └── routers/ HTTP endpoints
│ ├── auth.py
│ └── expenses.py
│
├── alembic/ Migrations
├── tests/ pytest tests
├── .github/workflows/ci.yml CI pipeline
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
