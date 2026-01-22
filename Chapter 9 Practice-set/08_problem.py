with open("this.txt") as f:
    content = f.read()

with open("copy_this.txt", 'w') as w:
    w.write(content)

with open('copy_this.txt') as a:
    if(a.read() != ""):
        print('mission accomplish.')
    else:
        print('file is empty.')