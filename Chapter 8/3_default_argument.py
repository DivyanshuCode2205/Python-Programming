def greet(name = "Divyanshu", ending = "Have a good day."):
    print(f"{name}, {ending}")

greet() # if didn't supply anything, it will use default values that is 'Divyanshu' and 'Have a good day.'
greet("Rohan", "have a coffee.") # if argument(s) is/are supplied then whole function will work with it.
