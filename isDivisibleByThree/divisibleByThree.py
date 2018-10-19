#!/usr/local/bin/python3
import argparse
from lib.ValidatorProcessor import ValidationProcessing  
from lib.DivisionProcessing import DivisionProcessing  

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', required=True, type=int, help="--number NUMBER")
    args = parser.parse_args()
    vp = ValidationProcessing(vars(args))
    if not vp.is_positive():
        print("Number is not positive")
        exit()
    dp = DivisionProcessing()
    if dp.checkDivisibleByThree(vp.number):
        print("Divisible by three")
    else:
        print("Not divisible by three")
#  This is main
if __name__ == "__main__":
    main()