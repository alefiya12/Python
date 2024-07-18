# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
num1 = int(input("Enter Number 1: ")) # User Input
num2 = int(input("Enter Number 2: ")) # User Input
num3 = int(input("Enter Number 3: ")) # User Input

if num1==num2 or num1==num3 or num2==num3: # If values are Equal Sum will be 0
	summ=0
else:
	summ=num1+num2+num3 # Calculating Sum
print("Sum: ",summ)