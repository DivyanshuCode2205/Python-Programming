dict_1 = {"Car" : "BMW", "Bike" : "Royal Enfield", "Rating" : 10, "Devices" : "Custom OS"
        , "email" : "divyanshuxd3@gmail.com"}

# .items()

print(f"Dictionary as list of (key, value) tuples: {dict_1.items()}") # Returns a list [not actually a list] of (key,value)tuples

'''
.items(), .keys(), .values() all three returns view objects

Q. What is view object in Python ?
View objects in Python are like live window to a dictionary where we can see the changes made to it (if any).
It access the dictionary's data without creating a copy of it.
It reflects the current state of dictionary. If someone tries to change the dictionary, what you see through
the window(i.e. view object) changes at the same time.

'''

# .keys()

print(f"List of keys in Dictionary: {dict_1.keys()}") # Returns list containing dictionary keys

# .update()

dict_1.update({"Profession" : "Software Developer"}) # updates the dictionary with supplied key-value pair
print(f"New element is added to dictionary {dict_1}")



'''Removing Dictionary items'''

del dict_1["email"] # removes item by key
print(dict_1)

element_poped = dict_1.pop("Devices") # removes item by key and returns its value
print(element_poped)

key, value = dict_1.popitem() # removes last key-value pair and returns its value
print(f"key : {key}, value : {value}")

dict_1.clear() # empties the dictionary