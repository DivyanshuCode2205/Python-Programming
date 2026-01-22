# enumerate function returns pair of index and items(i.e. tuple datatype) of list/tuples

l = ['ChatGPT', 'Gemini', 'Perplexity AI', 'Claude AI', 'Co-Pilot']

x = enumerate(l)
print(list(x))

for index, item in enumerate(l):
    print(f'Go for -> {index + 1}. {item}')
