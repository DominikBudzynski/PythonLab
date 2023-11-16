
class Fibonacci:
    def __init__(self, steps):
        self.steps = steps
        self.currentIt = 1
        self.prevIt = 0
        self.currentVal = 0
    
    def  __iter__(self):
        return self
        
    def __next__(self):
        if (self.currentVal >= self.steps):
            raise StopIteration
        else:
            result = self.prevIt            
            self.prevIt, self.currentIt = self.currentIt, self.currentIt + self.prevIt            
            self.currentVal += 1
            return result
        
if __name__ == "__main__":
    steps = 6
    fib = Fibonacci(steps)
    for num in fib:
        print(num)