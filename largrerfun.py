def largest_of_three(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    top_three = sorted_numbers[:3]
    return top_three[0]
numbers = [12, 45, 7, 32, 89, 54, 23]
result = largest_of_three(numbers)
print("The largest number among the top three is:", result)
print("veena-ec072")
