def summation(n):
    if(n == 0 or n == 1):
        return 1
    
    sum = n + summation(n  - 1)
    return sum

number = int(input("Enter number: "))

print(f"Sum of first {number} natural numbers = {summation(number)}")
