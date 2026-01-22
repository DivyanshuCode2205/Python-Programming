"""
For n = 3

  *
 ***
*****

"""

'''
Things to be noted from this star pattern like :

First line has 2 spaces and 1 star, whereas second line has 1 space and 3 stars in similar way third line has
0 space and 5 stars.

'''

"""For visible star pattern the value of n must be from n = 3 to n = 70"""

n = int(input("Enter: "))

for i in range(1, (n + 1)):
    print(" " * (n - i), end="") # end = "" --> removes by-default new line provided by print()
    print("*" * ((2*i) - 1), end="") # foumula for generating odd number sequence
    print("") # it adds default newline provided by print()
