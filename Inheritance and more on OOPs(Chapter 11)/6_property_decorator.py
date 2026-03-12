# it makes methods/functions act as an attribute

# so, instead of obj.method() you can write obj.method (without parenthisis)

# this can be used when you want an attribute to be read-only or to be computed on the fly

class Circle:
    def __init__(self, radius):
        self.r = radius

    @property
    def area(self): # here function acts as an attribute and it can't be changed directly
        return (3.14 * (self.r ** 2))
    
a = Circle(5)
print(f'Area of circle {a.area}')
