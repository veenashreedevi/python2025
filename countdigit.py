def count_digits(number):
    # Convert the number to a string and count the length
    return len(str(abs(number)))  # abs() handles negative numbers

# Test the function
num = 123456
print(f"The number of digits in {num} is {count_digits(num)}")
