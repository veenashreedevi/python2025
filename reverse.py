def reverse_number(number):
    return int(str(number)[::-1])
num = int(input("Enter an integer: "))
reversed_num = reverse_number(num)
print(f"The reverse of {num} is {reversed_num}.")
