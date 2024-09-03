# Write a Python program to count the number of lines in a text file.
file = open("example.txt", "r") # Open file in read mode

# Reading all lines at once and storing them in a list
lines = file.readlines()

count=0
# Iterating through each line and stripping any trailing newline characters
for line in lines:
    count=count+1

print("Number of lines in Code are:",count)
file.close()  # Close File