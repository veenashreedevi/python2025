def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    if sum_of_powers == number:
        return True
    else:
        return False
num = 153
print("VEENA-EC072")
result = is_armstrong_number(num)
if result:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
