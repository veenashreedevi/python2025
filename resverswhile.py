def reverse_number(number):
    number = abs(number)
    while number > 0:
        digit = number % 10
        print(digit, end="")
        number //= 10
num = 12345
print(f"Reversed number of {num} is: ", end="")
reverse_number(num)
