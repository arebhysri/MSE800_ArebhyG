import unittest
from tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        self.tracker.add_expense("Lunch", 12.5)
        self.assertEqual(len(self.tracker.expenses), 1)
        self.assertEqual(self.tracker.expenses[0].description, "Lunch")

    def test_total_expense(self):
        self.tracker.add_expense("Coffee", 3.0)
        self.tracker.add_expense("Book", 15.0)
        self.assertEqual(self.tracker.calculate_total(), 18.0)

    def test_negative_expense(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense("Invalid", -5.0)

if __name__ == "__main__":
    unittest.main()

