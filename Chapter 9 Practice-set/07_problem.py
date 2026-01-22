with open('log.txt', 'r') as f:
    data = f.readlines()# returns list of read lines

count_line = 1

for line in data:
    if('python' in line):
        print(f"line number where python is present {count_line}")
        break

    count_line += 1
else:
    print("Python is not present.")