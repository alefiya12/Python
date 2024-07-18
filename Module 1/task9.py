# Write a python program to sum of the first n positive integers.
num = int(input("Enter a Number: ")) # User Input
summ=0
for i in range(num+1): # sum of n positive integers
	summ=summ+i
print("Sum of First",num,"numbers is: ",summ)