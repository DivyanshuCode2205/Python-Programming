class Complex:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary
        
    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i) # returns new complex object
    
    def __mul__(self, other):
        real_part = self.r*other.r - self.i*other.i
        imaginary_part = self.r*other.i + self.i*other.r
        return Complex(real_part, imaginary_part) # gives new Complex object
    
    def __str__(self):
        return f'{self.r} + {self.i}i'
    
c1 = Complex(3, 4)
c2 = Complex(5, 6)
c3 = c1 + c2 # here c3 is new complex class's object
c4 = c1 * c2
print(str(c3))
print(str(c4))
