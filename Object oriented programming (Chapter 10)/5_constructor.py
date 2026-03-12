class Student:

    language = 'C' # this is class attribute

    def __init__(self, name, standard, roll, language):# dunder method which is automatically called as soon as object is created
        
        # all these four are instance attributes not class attribute, means each object has their own attribute

        self.name = name
        self.standard = standard
        self.roll = roll
        self.language = language

        print('Object is created.')

a = Student('Divyanshu', '12th', 12, 'Python') # equivalent to student.__init__(a, 'Divyanshu', '12th', roll)
print(f"{a.name}\n{a.standard}\n{a.roll}\n{a.language}")
