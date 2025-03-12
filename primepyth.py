def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(number**0.5) + 1):  # Check divisibility up to the square root of the number
        if number % i == 0:
            return False  # If divisible, it's not a prime number
    return True  # If no divisors are found, it's a prime number

# Input: Take the number from the user
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
