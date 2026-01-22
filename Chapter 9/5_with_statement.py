'''to open and close a file automatically use with statement'''

# it's just a syntactic sugar for open() and close()

# for example

f = open("myfile_1.txt")
print(f"{f.read()}")
f.close() # here we have to use close() to explicitly close the file

# now, using with statement opening and closing gets automatic

with open("myfile_2.txt") as f:
    print(f"{f.read()}")


'''
you can access multiple files by single with statement by using parethesis

syntax:

with(
    open('file_1.txt) as f1,
    open('file_2.txt) as f2
):

Do whatever you need to do now.

'''