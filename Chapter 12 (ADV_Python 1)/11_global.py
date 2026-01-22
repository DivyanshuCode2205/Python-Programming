x = 10 # global variable (outside variable), it can use inside of a function and outside of a function

def fx():
    global x # changes the value of global variable x
    x = 20 # local variable, it only exits inside the function
    print(x)

fx() # prints value of x inside of it
print(x) # prints the outside variable
