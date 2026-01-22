numbers = [] # empty list

for i in range(0, 4):
    user = int(input("Enter number: "))
    numbers.append(user)

print(f"The list of number {numbers}")

if(numbers[0] > numbers[1] and numbers[0] > numbers[2] and numbers[0] > numbers[3]):
    print(f"{numbers[0]} is greatest among others.")

elif(numbers[1] > numbers[0] and numbers[1] > numbers[2] and numbers[1] > numbers[3]):
    print(f"{numbers[1]} is greatest among others.")

elif(numbers[2] > numbers[0] and numbers[2] > numbers[1] and numbers[2] > numbers[3]):
    print(f"{numbers[2]} is greatest among others.")

else:
    print(f"{numbers[3]} is greatest among others.")