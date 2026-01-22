from functools import reduce

l = [i for i in range(1, 51)]
print(l)

def greater(a, b):
    if(a > b):
        return a
    else:
        return b

result = reduce(greater, l)

print(result)
