list_int = [1, 2, 3, 4, 5, 6, 7]

for index, item in enumerate(list_int):
    if(index == 2 or index == 4 or index == 6):
        print(list_int[index])

# or
'''
for i in range(2, len(list_int), 2):
    print(list_int[i])
'''
