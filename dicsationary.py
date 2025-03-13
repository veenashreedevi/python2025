# Creating a sample dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 1. Accessing values using keys
print("Accessing values by key:")
print("Name:", my_dict["name"])  # Access value using key
print("Age:", my_dict["age"])

# 2. Adding a new key-value pair to the dictionary
my_dict["email"] = "alice@example.com"  # Adding new key-value pair
print("\nAfter adding new key-value pair (email):", my_dict)

# 3. Updating an existing key's value
my_dict["age"] = 26  # Updating the value for the key 'age'
print("\nAfter updating age:", my_dict)

# 4. Removing a key-value pair using 'del'
del my_dict["city"]  # Remove the key-value pair with key 'city'
print("\nAfter deleting 'city' key:", my_dict)

# 5. Removing a key-value pair using 'pop' (returns the value)
email_value = my_dict.pop("email")  # Remove 'email' and return its value
print("\nAfter popping 'email' key:", my_dict)
print("Popped email value:", email_value)

# 6. Getting all keys, values, and items from the dictionary
print("\nGetting all keys:", my_dict.keys())
print("Getting all values:", my_dict.values())
print("Getting all items (key-value pairs):", my_dict.items())

# 7. Checking if a key exists in the dictionary
if "name" in my_dict:
    print("\nKey 'name' exists in the dictionary.")
else:
    print("\nKey 'name' does not exist in the dictionary.")

# 8. Iterating over the dictionary
print("\nIterating over the dictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# 9. Clearing the entire dictionary
my_dict.clear()  # Removes all items from the dictionary
print("\nAfter clearing the dictionary:", my_dict)
