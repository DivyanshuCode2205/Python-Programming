f = open("test_file.txt", "r")

line = f.readline()# reads single line from the given file
print(f"{line}")

lines = f.readlines()# reads all lines from the given file and return them as list
# each line in the list ends with '\n'

# print(lines) # prints the list

for l in lines:
    print(l)
print(type(lines))# retruns the class list

f.close()