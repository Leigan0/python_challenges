import unittest
from app.leap_year_checker import LeapYearChecker

class LeapYearCheckerSpec(unittest.TestCase):

    def test_leapYearChecker_is_divisible_by_four_returns_true(self):
        leapYearChecker = LeapYearChecker(4)
        self.assertEqual(leapYearChecker.is_divisible_by_four(), True)
    
    def test_leapYearChecker_is_divisible_by_four_returns_false(self):
        leapYearChecker = LeapYearChecker(6)
        self.assertEqual(leapYearChecker.is_divisible_by_four(), False)

    def test_leapYearChecker_is_not_divisible_by_100_returns_false(self):
        leapYearChecker = LeapYearChecker(100)
        self.assertEqual(leapYearChecker.is_not_divisible_by_one_hundred(), False)
    
    def test_leapYearChecker_is_not_divisible_by_100_returns_true(self):
        leapYearChecker = LeapYearChecker(101)
        self.assertEqual(leapYearChecker.is_not_divisible_by_one_hundred(), True)
    
    def test_leapYearChecker_is_divisible_by_400_returns_true(self):
        leapYearChecker = LeapYearChecker(400)
        self.assertEqual(leapYearChecker.is_divisible_by_four_hundred(), True)
    
    def test_leapYearChecker_is_divisible_by_400_returns_false(self):
        leapYearChecker = LeapYearChecker(402)
        self.assertEqual(leapYearChecker.is_divisible_by_four_hundred(), False)
    
    def test_leapYearChecker_is_a_leap_year_returns_true_1804(self):
        leapYearChecker = LeapYearChecker(1804)
        self.assertEqual(leapYearChecker.is_a_leap_year(), True)
    
    def test_leapYearChecker_is_a_leap_year_returns_false_1805(self):
        leapYearChecker = LeapYearChecker(1805)
        self.assertEqual(leapYearChecker.is_a_leap_year(), False)



