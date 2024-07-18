# Write a Python program to get the Factorial number of given number.
num = int(input("Enter a Number: ")) # User Input
fact = 1
for i in range(2,num+1): # Calculating Factorial
	fact *= i
print("Factorial: ", fact)