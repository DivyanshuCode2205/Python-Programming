class Employee: # Parent/Base class

    company = 'Google' # class attribute

    def __init__(self, name, salary, exprience):
        self.name = name
        self.salary = salary
        self.exprience = exprience

    def details(self):
        print(f'The name is {self.name}, salary is {self.salary} & years of work exprience {self.exprience}')

'''
Here, I used some of the part of class Employee in class Programmer, but if I made some changes to class Employee
then I have to manually change the other class Programmer which may be prone to error while doing so.
'''

# class Programmer:

#     company = 'Space X'
#     def details(self):
#         print(f'The name is {self.name}, salary is {self.salary} & years of work exprience {self.exprience}')

#     def showLanguage(self):
#         print(f'{self.name} is good with {self.language}')

'''
Using concept of inheritance
'''

class Programmer(Employee): # Inheritance/Child class

    company = 'Tesla'
    language = 'Python'
    
        
    def showLanguage(self):
        print(f'{self.name} is good with {self.language} working at {self.company}')

a = Employee('Divyanshu', 1000000, 15)
a.details()

b = Programmer('Divyanshu', 1000000, 15)
b.showLanguage()