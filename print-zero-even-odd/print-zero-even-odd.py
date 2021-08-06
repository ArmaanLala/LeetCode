from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.locks = [Lock(),Lock(),Lock()]
        self.locks[1].acquire()
        self.locks[2].acquire()
        self.val = 0
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range (self.n):
            self.locks[0].acquire()
            printNumber(0)
            self.val += 1
            self.locks[(self.val % 2) + 1].release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.locks[1].acquire()
            printNumber(i)
            self.locks[0].release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.locks[2].acquire()
            printNumber(i)
            self.locks[0].release()
            
        