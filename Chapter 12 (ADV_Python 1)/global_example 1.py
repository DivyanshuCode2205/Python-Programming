x = 60

def change():
    global x # instructs python to change value of variable(i.e x) out of its scope
    x = 80
    print('value of x inside', x)

change()
print(x) # global variable is now changed
