letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
name = input("Enter name: ")
date = input("Enter date: ")

# first we replace <|Name|> with name
# we got a string where <|Name|> is replaced
# then in the string we replaced <|Date|> with date
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))