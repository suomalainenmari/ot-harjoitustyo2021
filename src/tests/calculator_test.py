import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_constructor_sets_correct_result(self):
        result = str(self.calculator.result)
        self.assertEqual(result, "0.0")

    def test_add_returns_correct_result(self):
        self.calculator.add(4)
        result = str(self.calculator.result)
        self.assertEqual(result, "4.0")

    def test_subtract_returns_correct_result(self):
        self.calculator.subtract(5)
        result = str(self.calculator.result)
        self.assertEqual(result, "-5.0")

    def test_multiply_returns_correct_result(self):
        self.calculator.add(2)
        self.calculator.multiply(4)
        result = str(self.calculator.result)
        self.assertEqual(result, "8.0")

    def test_divide_returns_correct_result(self):
        self.calculator.add(20)
        self.calculator.divide(10)
        result = str(self.calculator.result)
        self.assertEqual(result, "2.0")

    def test_all_clear_sets_result_to_zero(self):
        self.calculator.add(10)
        self.calculator.clear()
        result = str(self.calculator.result)
        self.assertEqual(result, "0.0")

    def test_divide_by_zero_returns_zero(self):
        self.calculator.add(10)
        self.calculator.divide(0)
        result = self.calculator.result
        self.assertEqual(result, "Error")
