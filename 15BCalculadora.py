def calculator(a, b, operation):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
    }

    func = operations.get(operation)

    if func:
        return func(a, b)
    else:
        return "Invalid operation"

import unittest

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator(5, 3, "add"), 8)

    def test_subtract(self):
        self.assertEqual(calculator(9, 4, "subtract"), 5)

    def test_multiply(self):
        self.assertEqual(calculator(3, 3, "multiply"), 9)

    def test_divide(self):
        self.assertEqual(calculator(10, 2, "divide"), 5)
        self.assertEqual(calculator(10, 0, "divide"), "Cannot divide by zero")

    def test_invalid_operation(self):
        self.assertEqual(calculator(5, 3, "modulus"), "Invalid operation")

if __name__ == "__main__":
    unittest.main()
