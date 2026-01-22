dict_1 = {'a':1, 'b':2}
dict_2 = {'b':2, 'c':3}
dict_3 = {'c':3, 'd':4, 'e':5}

merged = dict_1 | dict_2
print(f'Merged dictionary: {merged}') # both the dictionaries merged and creates another dictionary

print(f'Dictionary before update: {dict_1}')

#update
dict_1 |= dict_3

print(f'Dictionary after update: {dict_1}') # updates the existing dict_1 dictionary with the key-value pairs of dict_3
