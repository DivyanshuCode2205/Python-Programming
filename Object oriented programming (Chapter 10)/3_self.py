class company:
    name = 'Google'
    CEO = 'Sundar Pichai'
    salary = '1.2 Billion'
    product = 'Gemini'

    def greet(self): # self refers to instance of class(i.e. object)
        print(f"Good morning {self.CEO}") # you may use self or not in function defined in class

a = company()
a.greet() # equivalent to company.greet(a)

print(f'{a.name}\n{a.salary}\n{a.product}')

