score = 0

def add_score():
    global score
    score += 10

def show_score():
    return score

print(f'initial score {show_score()}')
add_score()
print(f'current score {show_score()}')
