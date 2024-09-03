#Write a Python program to read a file line by line and store it into a list
file = open("example.txt", "r")
line_list = []

# Reading all lines at once and storing them in a list
lines = file.readlines()

# Iterating through each line and stripping any trailing newline characters
for line in lines:
    line_list.append(line.strip())

print(line_list)
file.close() # Close File