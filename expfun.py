def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
base = 2
exponent = 5
result = power(base, exponent)
print("veena-ec072")
print(f"{base} raised to the power of {exponent} is: {result}")
