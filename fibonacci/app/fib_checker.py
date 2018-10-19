from fibonacci import FibonacciChecker
import argparse
i = input('Please enter a number ')
fib_checker = FibonacciChecker(i)
print('sum =')
print(fib_checker.sum())