import random

number_times = int(input("Enter number of times you want to play: "))

score_human = score_computer = 0

game_dict = {'s':1, 'w':2, 'g':3}
reverse_game_dict = {1:'Snake', 2:'Water', 3:'Gun'}

for i in range(number_times):

    human = input("Enter your choice: ")

    value = game_dict[human]
    computer = random.choice([1,2,3])

    if(value == computer):
        print("The game is tied.")

    else:

        if((computer - value) == 1 or (computer - value) == -2):
            print(f"User chose {reverse_game_dict[2]} and computer chose {reverse_game_dict[3]}")
            print("")
            print("User won, computer lost.")
            print("")
            score_human += 1

        elif((computer - value) == 2 or (computer - value) == -1):
            print(f"User chose {reverse_game_dict[3]} and computer chose {reverse_game_dict[2]}")
            print("")
            print("Computer won, user lost.")
            print("")
            score_computer += 1

if(score_human > score_computer):
    print(f"Human won with score {score_human}")
    print("")

elif(score_human == score_computer):
    print(f"Draw, with score {score_human}")
    print("")

else:
    print(f"Computer won with score {score_computer}")
    print("")
