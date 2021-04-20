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

    def test_counter_number_converts_negative_to_positive(self):
        self.calculator.add(-7)
        self.calculator.counternumber()
        self.assertEqual(self.calculator.result, 7.0)

    def test_counter_number_converts_positive_to_negative(self):
        self.calculator.add(14)
        self.calculator.counternumber()
        self.assertEqual(self.calculator.result, -14.0)

    def test_to_percentage_returns_correct_value(self):
        self.calculator.add(88)
        self.calculator.to_percentage()
        self.assertEqual(self.calculator.result, 0.88)

    def test_many_calculations_in_a_row_returns_correct_value(self):
        self.calculator.add(5)
        self.calculator.subtract(20)
        self.calculator.multiply(2)
        self.calculator.divide(6)
        self.assertEqual(self.calculator.result, -5.0)
