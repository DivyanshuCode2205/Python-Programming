age = int(input("Enter your age: "))

# both the if statements are independent of each other.

# if statement 1.

if(age % 2 == 0):
    print(f"Age {age} is even.")

# if statement 2

if(age >= 18):
    print("Yes.")

elif(age <= 0):
    print("You are enterning invalid age.")

else:
    print("No.")
