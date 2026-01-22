from functools import reduce

# Map

l = [1, 2, 3, 4, 5, 6, 7]

square = lambda x : x * x

square_list = map(square, l)

# print(type(square_list)) # prints class map
print(list(square_list))

# Filter

even_number = lambda n : (n % 2 == 0)

even_list = filter(even_number, l)
print(list(even_list))

# Reduce

sum = lambda a, b : a + b

value = reduce(sum, l)
print(value)
