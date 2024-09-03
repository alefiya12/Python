# Write a Python program to copy the contents of a file to another file.
file1 = open("example.txt", "r") # Open file in read mode
file2 = open("example2.txt", "w") # Open file in write mode

file2.write("Text Copied from example.txt\n")
lines = file1.readlines() # Reading file1

for line in lines:
	file2.write(line) # Copyong file1 to file2

file1.close() # Close File1
file2.close() # Close File2

print("File example.txt copied to example2.txt")