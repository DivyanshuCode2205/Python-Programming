# unlike lists, tuples are immutable datatypes

a = () # empty tuple and type(a) retuns class <'tuple'>

# but if we do something like this b = (1) then type(b) would return class <'int'>

c = (1, 3, 5, 6, "Harry", "Jhoomka", 334, 706.4)
print(type(c))
