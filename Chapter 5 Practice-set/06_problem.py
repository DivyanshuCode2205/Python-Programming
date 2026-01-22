dictionary = {}

for i in range(0, 4):
    name = input("Enter your name: ")
    language = input("Enter your favourite language: ")
    dictionary.update({name:language})

print(dictionary)