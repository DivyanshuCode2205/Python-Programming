"""
* * * 
*   *
* * * 
"""

n = int(input("Enter: "))

for i in range(1, (n + 1)):
    if(i == 1 or i == n):
        print("* " * n) # adds newline automatically 
    else:
        print("*", end=" ")
        print("  " * (n - 2), end="")
        print("*") # adds newline automatically
