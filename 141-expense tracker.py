# Expense Tracker
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)

    def get_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense["category"] == category]

    def get_all_expenses(self):
        return self.expenses
# Example usage
tracker = ExpenseTracker()
tracker.add_expense(50, "Food", "Groceries")
tracker.add_expense(20, "Transport", "Bus ticket")
tracker.add_expense(30, "Food", "Dining out")
print("Total expenses:", tracker.get_total_expenses())  # Output: Total expenses: 100
print("Food expenses:", tracker.get_expenses_by_category("Food"))  # Output: Food expenses: [{'amount': 50, 'category': 'Food', 'description': 'Groceries'}, {'amount': 30, 'category': 'Food', 'description': 'Dining out'}]
print("All expenses:", tracker.get_all_expenses())  # Output: All expenses: [{'amount': 50, 'category': 'Food', 'description': 'Groceries'}, {'amount': 20, 'category': 'Transport', 'description': 'Bus ticket'}, {'amount': 30, 'category': 'Food', 'description': 'Dining out'}]