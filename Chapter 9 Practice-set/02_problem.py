import random as r

def game():
    
    print("You are playing game...: ")
    score = r.randint(1, 100)

    print(f"Your score {score}")

    with open("high Score.txt") as f:# opens the file in read mode
        high_score = f.read()
        if(high_score != ""): # condition for updating the high score
            high_score = int(high_score) # updates the high score

        else:
            high_score = 0
        
    if(score > high_score):# if score is greater than high score only then updates
        with open("high Score.txt", "w") as a:
            a.write(str(score))# write only accepts str arguments

    else:
        print(f"{score} < {high_score} so no update.")

game()