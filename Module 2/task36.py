# Write a Python program to calculate the area of a trapezoid
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height of the trapezoid: "))

if base1 <= 0 or base2 <= 0 or height <= 0:
    print("All dimensions must be positive numbers.")
else:
	area = 0.5 * (base1 + base2) * height
	print(f"\nThe area of the trapezoid is: {area}")