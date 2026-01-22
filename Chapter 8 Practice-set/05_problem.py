def stars(l):
    for i in range(1, (l + 1)): # i is from 1 to l
        
        print("*" * ((l + 1) - i), end="")
        print("")
    
lines = int(input("Enter number of lines: "))
stars(lines)