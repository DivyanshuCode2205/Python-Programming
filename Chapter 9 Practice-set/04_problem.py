with open('04_problem.txt') as f:
    content = f.read()# reads whole file as single string
    # print(content)

with open("04_problem.txt", "w") as f:
    
    content_new = content.replace('donkey', '######')
    f.write(content_new)
