# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
# Read input from the user
numbers_input = input("Enter decimal numbers separated by spaces: ")

numbers_str = numbers_input.split()

numbers = [float(num) for num in numbers_str]

max_number = max(numbers)
min_number = min(numbers)

print(f"Maximum number: {max_number}")
print(f"Minimum number: {min_number}")