def count_occurrences(numbers, element):
    count = numbers.count(element) 
    return count
numbers = [10, 20, 30, 20, 40, 20, 50]
element = 20
occurrences = count_occurrences(numbers, element)
print(f"The element {element} appears {occurrences} times in the list.")
print("VeenaEC-072")
