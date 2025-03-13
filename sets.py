# Creating a sample set
my_set = {10, 20, 30, 40, 50}

# 1. Adding an element to the set
my_set.add(60)  # Adds 60 to the set
print("After adding 60:", my_set)

# 2. Adding multiple elements using update
my_set.update([70, 80])  # Adds multiple elements (70, 80) to the set
print("\nAfter updating with multiple elements:", my_set)

# 3. Removing an element from the set using remove
my_set.remove(20)  # Removes 20 from the set
print("\nAfter removing 20:", my_set)

# 4. Removing an element using discard (no error if the element does not exist)
my_set.discard(100)  # Does nothing since 100 is not in the set
print("\nAfter discarding 100 (not in the set):", my_set)

# 5. Popping an arbitrary element from the set
popped_element = my_set.pop()  # Removes and returns an arbitrary element
print("\nAfter popping an element:", my_set)
print("Popped element:", popped_element)

# 6. Checking if an element exists in the set
print("\nChecking if 30 exists in the set:")
if 30 in my_set:
    print("30 is in the set.")
else:
    print("30 is not in the set.")

# 7. Set Operations:
# Union (combining two sets)
another_set = {50, 60, 70, 90}
union_set = my_set.union(another_set)
print("\nUnion of my_set and another_set:", union_set)

# Intersection (common elements between two sets)
intersection_set = my_set.intersection(another_set)
print("\nIntersection of my_set and another_set:", intersection_set)

# Difference (elements in my_set but not in another_set)
difference_set = my_set.difference(another_set)
print("\nDifference (elements in my_set but not in another_set):", difference_set)

# Symmetric Difference (elements in either set, but not in both)
symmetric_difference_set = my_set.symmetric_difference(another_set)
print("\nSymmetric Difference (elements in either set, but not both):", symmetric_difference_set)

# 8. Iterating over the set
print("\nIterating over the set:")
for item in my_set:
    print(item)

# 9. Getting the length of the set
set_length = len(my_set)
print("\nLength of the set:", set_length)

# 10. Clearing all elements from the set
my_set.clear()  # Removes all items from the set
print("\nAfter clearing the set:", my_set)
