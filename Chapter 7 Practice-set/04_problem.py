num = int(input("Enter number: "))

if(num <= 1):
    print('1 is neither prime nor composite')

elif(num == 2):
    print(f"Number {num} is the smallest prime number")

else:
    for i in range(2, num):
        if(num % i == 0):
            print(f"number {num} is not prime.")
            break

    else:
        print(f"number {num} is prime.")