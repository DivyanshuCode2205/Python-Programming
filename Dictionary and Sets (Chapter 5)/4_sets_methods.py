set_1 = {1, 4, 89, 56, 34, 21, "BMW", "Divyanshu", 46.54} # we can also add elements of different datatypes
# but it doesn't contains duplicate values
set_2 = {5, 89, "Ford", "Divyanshu", 46.54, "abc@gmail.com"}

# sets methods

# 1. add()

set_1.add(700)
print(f"Set after adding new element {set_1}")

# 2. len()

print(f"number of elements in set {len(set_1)}")

# 3. remove() --> raises key error if element is not found whereas discard() doesn't do so

set_1.remove(4)
print(f"updated set {set_1}")

# 4. pop() # removes and returns its value

print(f"it removes any random element from set {set_1.pop()}")
