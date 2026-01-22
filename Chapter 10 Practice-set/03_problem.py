class Code:
    a = 20 # class attribute

obj = Code() # object is created
obj.a = 0 # instance attribute

'''
instance attribute can also be deleted as:

del obj.a

in that case interpreter will check the class att. first
'''

# as we know that, instance attribute takes preference over class attribute during assingment & retrival
print(obj.a) # interpreter checks instance attribute first and doesn't bother checking the class attribute
# interpreter checks for object's own attribute first if not, then go for class attribute
print(Code.a) # class attribute a is still 20
