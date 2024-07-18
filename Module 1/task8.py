# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
a = int(input("Enter Number 1: ")) # User Input
b = int(input("Enter Number 2: ")) # User Input

if a == b or abs(a - b) == 5 or (a + b) == 5: # Checking if two integers or their difference is 5
    print("True")
else:
    print("False")