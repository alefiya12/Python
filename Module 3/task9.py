# Write a Python program to write a list to a file.
file = open("example.txt", "a") # Open file in append mode
list1 = ["List Element 1","List Element 2","List Element 3","List Element 4","List Element 5"]

# Iterating through each line and stripping any trailing newline characters
for line in list1:
	file.write("\n")
	file.write(line)

print("List Written in file")
file.close()  # Close File