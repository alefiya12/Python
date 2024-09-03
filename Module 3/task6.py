# Write a Python program to read a file line by line store it into a variable.
file = open("example.txt", "r")

# Reading all lines at once and storing them in a single variable
lines = file.readlines()

all_lines = ''.join(lines)  # If you want a single string

print(all_lines)  # Prints all lines as a single string or a list of lines

file.close()  # Close File
