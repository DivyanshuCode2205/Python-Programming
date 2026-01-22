num = int(input('Enter a number: '))

table_list = [num * i for i in range(1, 11)]

with open('Table.txt', 'a') as f: # now file wouldn't be overwrite

    f.write(str(table_list) + '\n')

print(type(table_list)) # type of table_list is still 'list'
