list = ["Apple", "Banana", "Grapes", 69.69, 69, 106, "Miles", "Shelby"]

element_pop = list.pop(4) # pop 69 element and return its value
print(f"The poped element is {element_pop}")

list.append("Divyanshu") # adds "Divyanshu" at the end of list
print(f"Updated list {list}")

print(list.index(69.69)) # gives index of element given as argument

list.insert(7, "7") # inserts element "7" at index 7, moves "Divyanshu" by 1 index forward
print(f"list after insertion {list}")

# creating another list

list_1 = [1, 2, 7, 8, 15, 21]
"""
list stores refernces/pointer to the objects rather than storing
objects themselves.This is the reason, why list can hold elements of different
datatypes, b'coz it dosen't care element's datatype only stores their refrences.
"""

"""
each integer (in this case) or any other element is a full fledged
object stored in seprate memory location unlike contiguously in C
"""

list_1.pop(5) # pops 21 out of the list
# or
# list_1.remove(21) # removes 21 from the list

list_1.append(22) # adds 22 at the end of list
print(f"New list: {list_1}")

list_1.sort() # arrange the list in ascending order
print(f"list in ascending order {list_1}")

list_1.reverse() # updates the list in reverse order
print(f"list in reverse order {list_1}")
