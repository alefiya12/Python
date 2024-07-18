# Write a Python program to count occurrences of a substring in a string.
main_string = input("Enter the main string: ") # User Input
substring = input("Enter the substring to count: ") # User Input
count = main_string.count(substring) # Counting occurences of substring
print(f"The substring '{substring}' occurs {count} times in the main string.")