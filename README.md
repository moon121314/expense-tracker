# 💰 Expense Tracker API

A production-style REST API for tracking personal expenses, built with **FastAPI, PostgreSQL, and JWT authentication**. Includes Docker, automated testing with **91% test coverage**, and GitHub Actions CI.

![CI](https://github.com/moon121314/expense-tracker/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Coverage](https://img.shields.io/badge/Coverage-91%25-brightgreen)

**🔗 Live Demo:** https://expense-tracker-adds.onrender.com/docs

> **Note:** Hosted on Render's free tier. The first request after inactivity may take approximately 60 seconds to respond.

## ✨ Features

* 🔐 User registration and login with JWT authentication
* 🔒 Secure password hashing with pwdlib and bcrypt
* 👤 User-scoped data isolation
* 📝 Full CRUD operations for expenses
* 🔍 Filtering by category and minimum amount
* 📄 Pagination using `skip` and `limit`
* ✅ Request and response validation with Pydantic
* 🏗️ Layered architecture for maintainability and testability
* ⚙️ Centralized configuration with `pydantic-settings`
* 🗄️ PostgreSQL database with SQLAlchemy ORM
* 🔄 Database migrations with Alembic
* 🧪 91% test coverage with pytest (11 tests)
* 🚀 GitHub Actions CI with pytest and Ruff
* 🐳 Docker and Docker Compose support
* ☁️ Cloud deployment using Render and Neon

## 🏗️ Architecture

```text
HTTP Client
    ↓
Routers       → HTTP endpoints
    ↓
Services      → Business logic
    ↓
CRUD          → Database operations
    ↓
SQLAlchemy    → ORM
    ↓
PostgreSQL    → Database
```

**Architecture rule:** Routers call services, services call CRUD, and CRUD handles database operations.

## 🛠️ Tech Stack

| Layer            | Technology               |
| ---------------- | ------------------------ |
| Language         | Python 3.12              |
| Framework        | FastAPI                  |
| Database         | PostgreSQL 16            |
| ORM              | SQLAlchemy 2.x           |
| Migrations       | Alembic                  |
| Authentication   | JWT, python-jose, pwdlib |
| Validation       | Pydantic                 |
| Configuration    | pydantic-settings        |
| Testing          | pytest, TestClient       |
| Linting          | Ruff                     |
| Containerization | Docker, Docker Compose   |
| CI               | GitHub Actions           |
| Hosting          | Render, Neon             |

## 📁 Project Structure

```text
expense-tracker-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── deps.py
│   ├── models/
│   │   ├── user.py
│   │   └── expense.py
│   ├── schemas/
│   │   ├── user.py
│   │   └── expense.py
│   ├── crud/
│   │   ├── user.py
│   │   └── expense.py
│   ├── services/
│   │   ├── auth_service.py
│   │   └── expense_service.py
│   └── routers/
│       ├── auth.py
│       └── expenses.py
├── alembic/
├── tests/
├── .github/workflows/ci.yml
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/moon121314/expense-tracker.git
cd expense-tracker
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and configure your PostgreSQL database URL, JWT secret, and other required settings.

```bash
cp .env.example .env
```

**Never commit your `.env` file or production secrets to GitHub.**

### 5. Run database migrations

```bash
alembic upgrade head
```

### 6. Start the API

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation:

**http://127.0.0.1:8000/docs**

## 🐳 Run with Docker

```bash
docker compose up --build
```

To stop the containers:

```bash
docker compose down
```

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

Run the linter:

```bash
ruff check app/ tests/
```

## 🔄 CI Pipeline

GitHub Actions automatically runs the test suite and Ruff checks on every push and pull request, helping maintain code quality and catch regressions early.

## 🔐 Security and Design

* JWT-based authentication for protected endpoints
* Password hashing instead of storing plaintext passwords
* User-level authorization and data isolation
* Pydantic validation for incoming requests
* Environment-based configuration for secrets
* Database migrations for controlled schema changes
* Separation of HTTP handling, business logic, and database operations

## 🎯 Project Goals

This project demonstrates practical backend engineering skills, including REST API development, authentication, relational database design, automated testing, containerization, CI, and cloud deployment.

**GitHub:** https://github.com/moon121314/expense-tracker

**Live API Documentation:** https://expense-tracker-adds.onrender.com/docs