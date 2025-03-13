#sample tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Accessing elements in the tuple (indexing)
print("Accessing elements by index:")
print("Element at index 0:", my_tuple[0])  # Access the first element
print("Element at index 3:", my_tuple[3])  # Access the fourth element

# 2. Slicing the tuple
print("\nSlicing the tuple:")
print("Elements from index 1 to 3:", my_tuple[1:4])  # Slice from index 1 to 3

# 3. Concatenating tuples
another_tuple = (60, 70)
concatenated_tuple = my_tuple + another_tuple  # Concatenate two tuples
print("\nAfter concatenating another tuple:", concatenated_tuple)

# 4. Repeating elements in a tuple
repeated_tuple = my_tuple * 2  # Repeat the tuple twice
print("\nAfter repeating the tuple:", repeated_tuple)

# 5. Checking if an element exists in the tuple
print("\nChecking if an element exists in the tuple:")
if 30 in my_tuple:
    print("30 is in the tuple.")
else:
    print("30 is not in the tuple.")

# 6. Iterating over the tuple
print("\nIterating over the tuple:")
for item in my_tuple:
    print(item)

# 7. Getting the length of a tuple
tuple_length = len(my_tuple)
print("\nLength of the tuple:", tuple_length)

# 8. Counting the occurrences of an element
count_30 = my_tuple.count(30)
print("\nThe number of times 30 appears in the tuple:", count_30)

# 9. Finding the index of an element
index_of_40 = my_tuple.index(40)
print("\nThe index of element 40:", index_of_40)

# Creating a sample tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Accessing elements in the tuple (indexing)
print("Accessing elements by index:")
print("Element at index 0:", my_tuple[0])  # Access the first element
print("Element at index 3:", my_tuple[3])  # Access the fourth element

# 2. Slicing the tuple
print("\nSlicing the tuple:")
print("Elements from index 1 to 3:", my_tuple[1:4])  # Slice from index 1 to 3

# 3. Concatenating tuples
another_tuple = (60, 70)
concatenated_tuple = my_tuple + another_tuple  # Concatenate two tuples
print("\nAfter concatenating another tuple:", concatenated_tuple)

# 4. Repeating elements in a tuple
repeated_tuple = my_tuple * 2  # Repeat the tuple twice
print("\nAfter repeating the tuple:", repeated_tuple)

# 5. Checking if an element exists in the tuple
print("\nChecking if an element exists in the tuple:")
if 30 in my_tuple:
    print("30 is in the tuple.")
else:
    print("30 is not in the tuple.")

# 6. Iterating over the tuple
print("\nIterating over the tuple:")
for item in my_tuple:
    print(item)

# 7. Getting the length of a tuple
tuple_length = len(my_tuple)
print("\nLength of the tuple:", tuple_length)

# 8. Counting the occurrences of an element
count_30 = my_tuple.count(30)
print("\nThe number of times 30 appears in the tuple:", count_30)

# 9. Finding the index of an element
index_of_40 = my_tuple.index(40)
print("\nThe index of element 40:", index_of_40)

# 10. Nested tuple
nested_tuple = (1, 2, (3, 4, 5), 6)
print("\nAccessing a nested tuple:")
print("Element at index 2, which is a tuple:", nested_tuple[2])
print("Accessing an element inside the nested tuple:", nested_tuple[2][1])  # Accessing 4 from (3, 4, 5)

nested_tuple = (1, 2, (3, 4, 5), 6)
print("\nAccessing a nested tuple:")
print("Element at index 2, which is a tuple:", nested_tuple[2])
print("Accessing an element inside the nested tuple:", nested_tuple[2][1])  # Accessing 4 from (3, 4, 5)
