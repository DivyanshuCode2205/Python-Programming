with open("poem.txt", "w") as f:
    
    poem = """
Twinkle twinkle little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle twinkle little star
How I wonder what you are
Twinkle twinkle little star
Shining brightly and afar
Twinkle star dust all around
From the sky right to the ground
Twinkle twinkle little star
Shining brightly and afar
"""
    f.write(poem)

with open("poem.txt") as a:
    lines = a.readlines()# returns list of line
    # print(lines)

    for item in lines:

        if(item == '\n'):# skips the iteration
            continue

        elif("twinkle" in item):# checks if the word 'twinkle' is in item
            print("Yes it contains word twinkle.")
            break

        else:
            print("No it doesn't contain word twinkle.")
