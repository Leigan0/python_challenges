class FibonacciChecker():
    def __init__(self, number):
        self.number = number
    
    def fib_sequence(self):
        first = 0
        second = 1
        fib_seq = []
        while first < self.number:
            print first
            fib_seq.append(first)
            next_num = first
            first = second
            second = next_num + second
        return fib_seq

    
    
