def compare(a, b, c):
    if(a > b and a > c):
        print(f"{a} is greatest")
    elif(b > a and b > c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

l = []
for i in range(0, 3):
    num = int(input("Enter number: "))
    l.append(num)

compare(l[0], l[1], l[2])

# x = int(input("Enter: "))
# y = int(input("Enter: "))
# z = int(input("Enter: "))
# compare(x, y, z)
