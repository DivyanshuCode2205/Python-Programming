words = ['donkey', 'moron', 'foolish']

with open("05_problem.txt") as f:
    content = f.read()

for item in words:
    content = content.replace(item, "######")

with open("05_problem.txt", "w") as f:
    f.write(content)


'''
words = ['donkey', 'moron', 'foolish']

with open("05_problem.txt") as f:
    content = f.read()

for item in words:
    content_new = content.replace(item, "######")

with open("05_problem.txt", "w") as f:
    f.write(content_new)
'''