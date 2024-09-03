# Write a Python program to read first n lines of a file.
first_n_lines=int(input("Enter Number of lines to read: "))
file = open("example.txt","r") # Open file in read mode

for i in range(1,first_n_lines+1):
	line = file.readline() # Reading file
	if line:
		print(f"Line {i}: {line.strip()}") # Printing Each Line
	else:
		print("\nEntire file read. No more lines are available.")
		break

file.close() # Close File