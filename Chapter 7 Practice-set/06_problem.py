number = int(input("Enter number: "))

product = 1

for i in range(0, number):
    product *= (i + 1)

print(f"Factorial of {number} is {product}")