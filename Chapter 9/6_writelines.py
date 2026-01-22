lst_of_str = ["Line 1.\n, Line 2.\n, Line 3.\n ,Line 4."]
with open("myfile_3.txt", "w") as f:
    f.writelines(lst_of_str)

with open("myfile_3.txt") as a:
    print(a.read())