a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

try:
    print(f'Dividing {a} by {b} = {a/b}')

except:
    print('Division by zero is not good.')

else:
    print('Try block executed successfully.') # this will be executed only if try block executed
