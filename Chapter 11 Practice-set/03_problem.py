class Employee:
    def __init__(self, salary, increment):
        self._salary = salary
        self._increment = increment

    @property
    def Increment(self):
        return self._increment
    
    @property
    def SalaryAfterIncrement(self):
        return (self._salary + (self._salary * (self._increment/100)))
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, salary):
        self._increment = ((salary/self._salary) - 1 )* 100

e = Employee(10000, 20)
print(f'Increment {e.SalaryAfterIncrement}')
e.SalaryAfterIncrement = 12000
print(e.Increment)