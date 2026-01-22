name = ['Alex', 'Arnold', 'Ali', 'Robert', 'Chris', 'Jimmy', 'Chandler', 'Sumit', 'Rahul']

search = input("Enter name to be searched: ")

if(search in name):
    print(f"Yes, name is present {search}")

else:
    print(f"Nope.")