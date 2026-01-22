try:
    with open('file 1.txt') as f1:
        content_1 = f1.read()
        print(content_1)

except Exception as e: # Either you can use Exception or FileNotFoundError
    print(e)

try:
     with open('file 2.txt') as f2:
         content_2 = f2.read()
         print(content_2)

except Exception as e:
    print(e)

try:
    with open('file 3.txt') as f3:
        content_3 = f3.read()
        print(content_3)

except Exception as e:
    print(e)
    