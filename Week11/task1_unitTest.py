import unittest

def add(a, b):
    """add two numbers and return the result"""
    return a + b
def subtract(a, b):
    """subtract two numbers and return the result"""
    return a - b
def multiply(a, b):
    """multiply two numbers and return the result"""
    return a * b
def divide(a, b):
    """divide two numbers and return the result"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ValueError, divide, 5, 0)

if __name__ == "__main__":
    unittest.main()