# Encapsulation of this Class
# so that variables/attributes inside of it is not accessed or modified directly

class Student:
    def __init__(self, name, marks):
        self._name = name   # private variable (can't be accessed directly)
        self._marks = marks # private variable (can't be accessed directly)

    def get_marks(self): # getter method
        return self._marks
    
    def set_marks(self, marks): # setter method
        if(0 <= marks <= 100):
            self._marks = marks
            print('Marks changed.')
        
        else:
            print('Invalid Input.')

s = Student('Divyanshu', 80)
print(f'Marks: {s.get_marks()}')
s.set_marks(75)
print(f'New marks: {s.get_marks()}')
