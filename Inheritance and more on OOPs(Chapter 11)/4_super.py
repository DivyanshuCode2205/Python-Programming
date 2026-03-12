class Employee:
    a = 1

    def __init__(self):
        print('Constructor of Employee', end="")
        print('\n')

class Programmer(Employee):
    b = 2
    # inherited a = 1 property

    def __init__(self):
        print('Constructor of Programmer', end="")
        print('\n')

class Manager(Programmer):
    c = 3
    # inherited both a = 1 and b = 2 property

    def __init__(self):
        super().__init__() # calls __init__() from super class that is Programmer
        print('Constructor of Manager', end="")
        print('\n')

x = Employee()
print(f'Property that belongs only to Employee class {x.a}')

y = Programmer()
print(f'Property that belongs only to Programmer class is {y.b} and property that belongs to Employee class {y.a}')

z = Manager()
print(f'Property that belongs only to Manager class is {z.c} whereas property that belongs to Employee class and Programmer class are {z.a} and {z.b}')