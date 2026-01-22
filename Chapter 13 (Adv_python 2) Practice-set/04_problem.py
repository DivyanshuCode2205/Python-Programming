l = [i for i in range(1, 50, 3)]

numbers = lambda n : n % 5 == 0

result = filter(numbers, l)
print(list(result))
