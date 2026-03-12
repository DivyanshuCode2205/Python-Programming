class Student:
    def __init__(self, name, marks):
        self._name = name  # private variable can't be accessed directly
        self._marks = marks

    @property
    def name(self): # getter
        return self._name
    
    @property
    def marks(self):
        return self._marks
    
    @name.setter # property(name) setter
    def name(self, value):
        if(len(value) < 3):
            print('Invalid input.')
        
        else:
            self._name = value

s = Student('Divyanshu', 80)
print(f'{s.name} and {s.marks}')
s.name = 'Raj'
print(f'{s.name} and {s.marks}')