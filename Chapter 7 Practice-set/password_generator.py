from random import sample

length = int(input("Enter your desired length for the password: "))

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_chars = '@#$%&*'

passcode_str = lowercase + uppercase + numbers + special_chars # string concatenation

generated_passcode = ''.join(sample(passcode_str, length))
# print(type(generated_passcode))

print(f'Password generated: {generated_passcode}')
