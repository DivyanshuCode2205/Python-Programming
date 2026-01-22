from random import randint

random_number = randint(1, 100)
number_of_guess = 0

for i in range(1, 101):
    gussed_number = int(input('Enter your guess number: '))
    if (gussed_number == random_number):
        print(f'You guessed the right number: {random_number}')
        number_of_guess += 1
        break
    else:
        if (gussed_number > random_number):
            print('Guess lower.')
            number_of_guess += 1

        elif (gussed_number < random_number):
            print('Guess higher.')
            number_of_guess += 1

        else:
            pass
print(f'Your number guess is {number_of_guess}')
