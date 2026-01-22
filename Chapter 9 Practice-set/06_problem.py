with open('log.txt') as f:
    data = f.read()

if('python' in data):
    print('yes it is there.')
else:
    print('no it is not here.')

# if('python' in data):
#     data = data.replace('python', 'C')

# with open('log.txt', 'w') as a:
#     a.write(data)
