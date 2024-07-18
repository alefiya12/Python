# Write a Python program to get the Fibonacci series of given range.
num = int(input("Enter a Number: ")) # User Input
num1 = 0
num2 = 1
print("FIBONNACI SERIES")
print(num1,num2,end=" ")
for i in range(2,num): # Calculating Fibonnaci Series 
	num3 = num1+num2
	print(num3,end=" ")
	num1=num2
	num2=num3
print()