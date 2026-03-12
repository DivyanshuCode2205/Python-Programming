class Employee:

    name = 'Divyanshu'
    salary = 2400000
    exprience = 10

    def details(self):
        company = 'Space X'
        print(f'Name is {self.name}, salary is {self.salary} & years of exprience {self.exprience}')

class Coder:

    language = 'Python' # class attribute

    def printLanguages(self):

        print(f'Out of all languages your language is {self.language}')

class Programmer(Employee, Coder): # inherits methods and properties of both the classes

    company = 'Youtube'
    def showLanguage(self):
        print(f'Name of the programmer {self.name}, preffered language {self.language}')

a = Employee()
b = Programmer() # here b is object of both classes Employee and Coder

a.details()
b.printLanguages()
b.showLanguage()
