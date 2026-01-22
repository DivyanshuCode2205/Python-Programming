with open('old.txt') as f:
    data = f.read()

with open('renamed_by_python.txt', 'w') as fl:
    fl.write(data)