from abc import ABC, abstractmethod
# abc -> abstract base class module
class Shape(ABC): # ABC is helper class that lets you define abstract base class
    @abstractmethod
    def printArea(self):
        pass             # Shape class doesn't care about how the area is calculated

class Rectangle(Shape): # Rectangle is child class of Shape
    type = 'Rectangle'
    sides = 4

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def printArea(self):
        return (self.length * self.breadth)
    
class Square(Shape):
    type = 'Square'
    sides = 4

    def __init__(self, side):
        self.lenght = side
    
    def printArea(self):
        return (self.lenght ** 2)

a = Rectangle(5, 8)
print(f'Area of {a.type}: {a.printArea()}')

b = Square(4)
print(f'Area of {b.type}: {b.printArea()}')