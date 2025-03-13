# Function to find the largest and smallest number in a list
def find_max_min(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    
    return largest, smallest
numbers = [10, 20, 30, 40, 50]
largest, smallest = find_max_min(numbers)
print("Largest Number:", largest)
print("Smallest Number:", smallest)
print("veenaEC-072")
