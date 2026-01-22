'''
.items(), .keys(), .values() all three returns view objects

Q. What is view object in Python ?
View objects in Python are like live window to a dictionary where we can see the changes made to it (if any).
It access the dictionary's data without creating a copy of it.
It reflects the current state of dictionary. If someone tries to change the dictionary, what you see through
the window(i.e. view object) changes at the same time.

'''

dict_1 = {"Car" : "BMW", "Bike" : "Royal Enfield", "Rating" : 10, "Devices" : "Custom OS",
           "email" : "divyanshuxd3@gmail.com"}

view_obj_1 = dict_1.items() # returns view object not list 
print(f"view_obj_1 before update {view_obj_1}, {type(view_obj_1)}")

view_obj_2 = dict_1.keys() # again it returns a view object
print(f"keys before update {view_obj_2}")

view_obj_3 = dict_1.values()
print(f"value before update {view_obj_3}")

dict_1["City"] = "Mumbai" # adds a new key-value pair to dictionary

print(f"after dict_1 update {view_obj_1}")

print(f"key after update {view_obj_2}")

print(f"value after update {view_obj_3}")

