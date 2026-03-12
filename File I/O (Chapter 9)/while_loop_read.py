f = open("test_file.txt")

line = 'a' # I initialized line with a to enter the loop for the first iteration

while(line != ""):
    line = f.readline() # updates line again and again. At the end of the file readline() returns an empty string.
    print(line, end="") # end="" removes the default newline character

f.close()