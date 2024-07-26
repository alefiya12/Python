# Write a Python function to calculate the factorial of a number
import math
num = int(input("Enter a Number: "))

if num == 0 or num == 1:
    print(f"The factorial of {num} is 1.")
else:
    print(f"The factorial of {num} is {math.factorial(num)}")