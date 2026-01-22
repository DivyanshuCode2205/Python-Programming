l = ['apple', 'banana', 'cherry']
print(list(enumerate(l)))

for index, item in enumerate(l, start = 1): # starts index from 1 instead of 0
    print(f'{index} : {item}')
    