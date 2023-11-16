
class ComplexNumber:
    def __init__(self):
        self.re = 0
        self.im = 0

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)
    
    def __sub__(self, other):
        return ComplexNumber(self.re - other.re, self.im - other.im)
    
z1 = ComplexNumber(5, 3)
z2 = ComplexNumber(4, 2)
z3 = z1 + z2

print(str(z3.re) + " + " + str(z3.im) + "j")
