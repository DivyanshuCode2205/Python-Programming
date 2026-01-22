person = {"name" : "Divyanshu", "age" : 20, "city" : "Mumbai"}
items = list(person.items()) # items() gives dict_items that is view object which is converted to list of tuples
print(items)
print(type(items))

items.insert(2, ("country", "India")) # insert this tuple at index 2 of list
new_person = dict(items) # reconstruct dictionary from list of tuples
print(f"new items {new_person}")
