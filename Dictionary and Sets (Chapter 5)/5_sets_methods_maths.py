set_1 = {1, 4, 89, 56, 34, 21, "BMW", "Divyanshu", 46.54}

set_2 = {5, 89, "Ford", "Divyanshu", 46.54, "abc@gmail.com"}

# 1. union() or | both gives the same result

print(f"union of set_1 and set_2 {set_1.union(set_2)}")
 
# 2. intersection() or & both gives the same result

print(f"common element in both the sets {set_1.intersection(set_2)}")

# 3. clear()

# print(f"empty set, {set_1.clear()}")

# 4. differences() or -

print(f"Elements that are only in A and not in B {set_1 - set_2}") # returns set of elements that are in set_1 only removing the common area

# 5. symmetric difference or ^

# elements that are only in A or B not in both (i.e. common part)

print(f"Elements that are only in A or B {set_1.symmetric_difference(set_2)}")

# 6. issubset() retruns either True or False

print(f"set 2 is subset of set 1 {set_1.issubset(set_2)}")

# 7. issuperset()

print(f"set 2 is superset of set 1 {set_2.issuperset(set_1)}")

# 8. isdisjoint()

print(f"two sets are disjoint {set_1.isdisjoint(set_2)}")