# Write a Python program to calculate the area of a parallelogram
base = float(input("Enter the length of the base: "))
height = float(input("Enter the height of the parallelogram: "))

if base <= 0 or height <= 0:
	print("Both the base and the height must be positive numbers.")
else:
	area = base * height
	print(f"\nThe area of the parallelogram is: {area}")