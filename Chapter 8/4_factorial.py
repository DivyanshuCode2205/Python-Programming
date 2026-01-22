def factorial(number):

    if(number == 1): # base case that stops recursion when its done
        return 1
    
    else:
        return (number * factorial(number - 1))
    
n = int(input("Enter n: "))
print(f"Factorial of given number {factorial(n)}")