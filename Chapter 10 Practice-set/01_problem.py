class Programmer:

    company = 'Microsoft' # this is class attribute

    def __init__(self, name, age, exprience, salary):
        self.name = name # these are instance attributes
        self.age = age
        self.exprience = exprience
        self.salary = salary

s = Programmer('Soham', 22, 15, 1300000) # object is created and given arguments are assinged to object's attributes
print(f'Company where Programmer works:{s.company} Name of programmer:{s.name} Age of programmer:{s.age} Years of exprience:{s.exprience} Salary:{s.salary}')

r = Programmer('Robinson', 54, 31, 500000)
print(f'Company where Programmer works:{r.company} Name of programmer:{r.name} Age of programmer:{r.age} Years of exprience:{r.exprience} Salary:{r.salary}')