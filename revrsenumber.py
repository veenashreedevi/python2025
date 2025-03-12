def reverse_number(number):
    # Convert the number to a string, reverse it, and convert it back to an integer
    return int(str(number)[::-1])

# Input: Take the integer input from the user
num = int(input("Enter an integer: "))

# Output: Print the reverse of the number
reversed_num = reverse_number(num)
print(f"The reverse of {num} is {reversed_num}.")
