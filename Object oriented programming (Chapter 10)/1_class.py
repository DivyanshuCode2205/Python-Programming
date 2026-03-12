class employee:# class is defined named employee (it's the blueprint)

    """
    name, language, salary all three are class attributes means they belong to
    class employee and shared by all objects created from it.
    """
    
    name = "Divyanshu"
    language = 'Python'
    salary = 1200000

a = employee()# object a is created based on the blueprint (i.e. employee)

a.age = 20 # here age is instance (object) attribute

print(f"{a.name}\n{a.age}\n{a.language}\n{a.salary}")
