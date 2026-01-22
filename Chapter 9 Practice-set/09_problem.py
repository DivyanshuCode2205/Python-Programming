with open('file_1.txt') as f:
    content_1 = f.read()

with open('file_2.txt') as s:
    content_2 = s.read()

if(content_1 == content_2):
    print('Yes both the files are identicals.')
else:
    print('Nope they aren\'t.')