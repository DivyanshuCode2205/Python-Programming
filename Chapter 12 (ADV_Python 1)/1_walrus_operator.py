# := -> walrus operator
# this operator assings value to a variable and then returns the assinged value

if((n := len([1, 2, 3, 4, 5, 6])) > 3):
    print(f'List is too long than excepted {n} elements instead of 3')