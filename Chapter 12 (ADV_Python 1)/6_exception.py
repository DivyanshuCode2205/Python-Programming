try:
    a = int(input('Enter number: '))
    print(f'entered number is {a}')

except Exception as e:
    print(e)

# try-except block prevents the program from crashing
# it keeps the program continuity.

print('Code below try-except block will be executed without any interuption.')
