class ExpenseTracker:
    """Track and analyze expenses."""

    def __init__(self):
        """Initialize an empty expense tracker."""
        self.expenses = []

    def add_expense(self, amount: float, category: str) -> None:
        """Add an expense to the tracker."""
        self.expenses.append({
            "amount": amount,
            "category": category
        })

    def total_expenses(self) -> float:
        """Return the total amount of all expenses."""
        total = 0.0

        for item in self.expenses:
            total += item["amount"]

        return total

    def expenses_by_category(self) -> dict[str, float]:
        """Return total expenses grouped by category."""
        result = {}

        for item in self.expenses:
            category = item["category"]
            amount = item["amount"]

            if category not in result:
                result[category] = 0.0

            result[category] += amount

        return result

    def filter_expenses_by_min_amount(
        self,
        min_amount: float
    ) -> list[dict]:
        """Return expenses with amount >= min_amount."""
        result = []

        for item in self.expenses:
            if item["amount"] >= min_amount:
                result.append(item)

        return result

    def average_expense_amount(self) -> float:
        """Return average amount spent per expense."""
        if not self.expenses:
            return 0.0

        total = self.total_expenses()

        return total / len(self.expenses)

    def sort_expenses_by_amount(
        self,
        descending: bool = False
    ) -> list[dict]:
        """Return expenses sorted by amount."""
        return sorted(
            self.expenses,
            key=lambda item: item["amount"],
            reverse=descending
        )


# -------------------------
# Test the class
# -------------------------

tracker = ExpenseTracker()

tracker.add_expense(500.0, "food")
tracker.add_expense(200.0, "transport")
tracker.add_expense(300.0, "food")
tracker.add_expense(1000.0, "rent")


print(tracker.total_expenses())
# 2000.0

print(tracker.expenses_by_category())
# {'food': 800.0, 'transport': 200.0, 'rent': 1000.0}

print(tracker.filter_expenses_by_min_amount(300.0))
# [
#     {'amount': 500.0, 'category': 'food'},
#     {'amount': 300.0, 'category': 'food'},
#     {'amount': 1000.0, 'category': 'rent'}
# ]

print(tracker.average_expense_amount())
# 500.0

print(tracker.sort_expenses_by_amount())
# [
#     {'amount': 200.0, 'category': 'transport'},
#     {'amount': 300.0, 'category': 'food'},
#     {'amount': 500.0, 'category': 'food'},
#     {'amount': 1000.0, 'category': 'rent'}
# ]

print(tracker.sort_expenses_by_amount(descending=True))
# [
#     {'amount': 1000.0, 'category': 'rent'},
#     {'amount': 500.0, 'category': 'food'},
#     {'amount': 300.0, 'category': 'food'},
#     {'amount': 200.0, 'category': 'transport'}
# ]