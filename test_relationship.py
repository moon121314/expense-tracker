from app.database import SessionLocal
from app.models.user import User

db = SessionLocal()

user = db.query(User).filter(User.id == 1).first()

print("User:", user.email)
print("Expenses:")

for expense in user.expenses:
    print(
        "ID:", expense.id,
        "Amount:", expense.amount,
        "Category:", expense.category
    )

db.close()