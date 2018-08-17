import sys

class LeapYearChecker:
    def __init__(self, year):
        self.year = year
    
    def is_a_leap_year(self):
        return self.is_divisible_by_four_hundred() or (self.is_not_divisible_by_one_hundred() and self.is_divisible_by_four())
    
    def is_divisible_by_four(self):
        return self.year % 4 == 0
    
    def is_not_divisible_by_one_hundred(self):
        return self.year % 100 != 0
    
    def is_divisible_by_four_hundred(self):
        return self.year % 400 == 0

print(LeapYearChecker(int(sys.argv[1])).is_a_leap_year())

    
# Write a program to accept a year from the user and check whether it is a leap year.
# _Hint: If a year is divisible by 4 and not divisible by 100  or if the year is divisible by 400_