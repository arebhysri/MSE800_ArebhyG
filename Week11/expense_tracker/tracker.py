class Expense:
    def __init__(self, description: str, amount: float):
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description: str, amount: float):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.expenses.append(Expense(description, amount))

    def calculate_total(self) -> float:
        return sum(exp.amount for exp in self.expenses)

    def list_expenses(self):
        return [(exp.description, exp.amount) for exp in self.expenses]
