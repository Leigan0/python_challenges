class FibonacciChecker():
    def __init__(self, number):
        self.number = number
        self.fib_seq = self.fib_sequence()

    def fib_sequence(self):
        first = 0
        second = 1
        sequence = []

        while first <= self.number:
            sequence.append(first)
            next_num = first
            first = second
            second = next_num + second
        return sequence

    def sum(self):
        return sum(self.fib_seq)
        


    

