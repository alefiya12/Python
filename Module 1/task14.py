# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1 = input("Enter String 1: ") # User Input
str2 = input("Enter String 2: ") # User Input

# Swapping first 2 characters of the string
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

str = new_str1+" "+new_str2
print("Result: ",str)