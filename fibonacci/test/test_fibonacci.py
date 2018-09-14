import unittest
from app.fibonacci import FibonacciChecker

class FibonacciCheckerSpec(unittest.TestCase):

    def test_returns_returns_series_of_fibonacci_numbers_until_number(self):
        fibChecker = FibonacciChecker(8)
        self.assertEqual(fibChecker,20)

    def test_returns_returns_series_of_fibonacci_numbers_until_number_test_2(self):
        fibChecker = FibonacciChecker(7)
        self.assertEqual(fibChecker,12)

    def test_if_number_5_given_return_12(self):
        fibChecker = FibonacciChecker(8)
        self.assertEqual(fibChecker,12)
    
