# Write a Python program to read last n lines of a file.
n = int(input("Enter the number of last lines to read: "))

file = open("example.txt", "r")
lines = file.readlines()  # Read all lines into a list
file.close()

last_n_lines = lines[-n:]  # Get the last 'n' lines

for line in last_n_lines:
	print(line.strip())  # Remove newline characters when printing

file.close() # Close File