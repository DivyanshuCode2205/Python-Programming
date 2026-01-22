s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
print(f"length of set s is {len(s)}") # results 2

 # reason python converts int to float and then compares their value
 # this works only when numeric values are equal
 # if there is a fractional part comparison(i.e. ==) will return False