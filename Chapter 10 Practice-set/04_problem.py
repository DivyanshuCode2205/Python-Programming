class Calculator:
    
    def __init__(self, n):
        self.number = n

    @staticmethod
    def greet():
        print('Hello')

    def square(self):
        print(f'Square of {self.number} = {self.number * self.number}')
    
    def cube(self):
        print(f'Cube of {self.number} = {self.number * self.number * self.number}')
    
    def square_root(self):
        import math as m
        print(f'Square root of {self.number} = {m.sqrt(self.number)}')

num = int(input('Enter number: '))
c = Calculator(num)
print(f'Entered number is {c.number}')
c.greet()
c.square()
c.cube()
c.square_root()
