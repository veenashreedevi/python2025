def is_perfect_number(number):
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0: 
            divisors_sum += i
    return divisors_sum == number
num = 28
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
