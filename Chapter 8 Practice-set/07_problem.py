def func_strip(list, word):
    striped_list = []
    for item in list:
        if item != word:
            striped_list.append(item.strip())
    
    return striped_list

lst = ['  apple  ', '  cherry', 'grapes   ', 'Harry  ', '    bannana']
print(func_strip(lst, 'grapes   '))