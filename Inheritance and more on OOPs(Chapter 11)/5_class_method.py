class Cars:

    wheels = 4 # class attribute

    def __init__(self, name):
        self.brand = name

    @classmethod # class method changes the class attributes only
    def change_wheels(cls, number):
        cls.wheels = number # class attribute is changed
    
a = Cars('BMW')
print(f'Name : {a.brand}, Wheels : {a.wheels}')

a.change_wheels(2)
print(f'Name : {a.brand}, Wheels : {a.wheels}')
