from random import randint

number_of_guesses = 0
random_number = randint(1, 100)

g = -10

while(g != random_number):
    g = abs(int(input('Enter guessed number: ')))
    
    if(g > random_number):
        print('Guess lower.')
        number_of_guesses += 1
    
    elif(g < random_number):
        print('Guess higher.')
        number_of_guesses += 1
    
    else:
        pass

print(f'Number of guesses {number_of_guesses}')