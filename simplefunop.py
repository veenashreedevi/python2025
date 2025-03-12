def simple_calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."
num1 = 10
num2 = 5
operator = "+"
result = simple_calculator(num1, num2, operator)
print(f"Result: {result}")
print("VEENA-EC072")
