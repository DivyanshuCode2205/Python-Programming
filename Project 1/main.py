"""look for bonus track on chatgpt history to know
how many times computer chooses a
particular number."""

'''for fair result try for bigger sample like 20, 50, ...'''

import random

number_times = int(input("Enter number of times you want to play: "))

user_score = 0
computer_score = 0

user_dict = {"s" : 1, "w" : 2, "g" : 3}
reverse_dict = {1 : "Snake", 2 : "Water", 3 : "Gun"}


'''
runs the whole block of code again and again,
means you have to give input again and again also
value of computer will get updated again and again
'''

for i in range(0, number_times):

    user = input("Enter your choice: ")

    user_value = user_dict[user] # access user_dict value with the help of user
    computer = random.choice([1, 2, 3]) # gives random number from the collection of [1, 2, 3]

    if(user_value == computer):
        print(f"Match is draw, with scores {user_score}")
        print("") # just adds a newline for spacing

    else:

        if(user_value == 1 and computer == 2):
            print(f"User chose {reverse_dict[1]} and computer chose {reverse_dict[2]}")
            print("")
            print("User won, computer lost.")
            print("")
            user_score += 1
    
        elif(user_value == 1 and computer == 3):
            print(f"User chose {reverse_dict[1]} and computer chose {reverse_dict[3]}")
            print("")
            print("Computer won, user lost.")
            print("")
            computer_score += 1
    
        elif(user_value == 2 and computer == 1):
            print(f"User chose {reverse_dict[2]} and computer chose {reverse_dict[1]}")
            print("")
            print("Computer won, user lost.")
            print("")
            computer_score += 1

        elif(user_value == 2 and computer == 3):
            print(f"User chose {reverse_dict[2]} and computer chose {reverse_dict[3]}")
            print("")
            print("User won, computer lost.")
            print("")
            user_score += 1

        elif(user_value == 3 and computer == 1):
            print(f"User chose {reverse_dict[3]} and computer chose {reverse_dict[1]}")
            print("")
            print("User won, computer lost.")
            print("")
            user_score += 1

        elif(user_value == 3 and computer == 2):
            print(f"User chose {reverse_dict[3]} and computer chose {reverse_dict[2]}")
            print("")
            print("Computer won, user lost.")
            print("")
            computer_score += 1

if(user_score > computer_score):
    print(f"Human won with score {user_score}")
    print("")

elif(user_score == computer_score):
    print(f"Draw, with score {user_score}")
    print("")

else:
    print(f"Computer won with score {computer_score}")
    print("")
