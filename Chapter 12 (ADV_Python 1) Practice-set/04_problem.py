a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if(b == 0):
    raise ZeroDivisionError('INFINITE.')

else:
    print(f'Division of {a} by {b} = {a/b}')
    