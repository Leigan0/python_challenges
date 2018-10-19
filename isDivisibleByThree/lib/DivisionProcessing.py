class DivisionProcessing:
    def __init__(self):
        pass
    def checkDivisibleByThree(self, number):
        while number > 9:
            print("{} greater than 9".format(number))
            digit_list = list(str(number))
            number = sum([int(d) for d in str(number)])
            print("Total number is {}".format(number))
        if number in (3,6,9):
            return True
        else:
            return False