# Write a Python function to reverses a string if its length is a multiple of 4.
str1 = input("Enter a String: ") # User Input
print("Length of String: ",len(str1))
if len(str1)%4==0:
	print("Reversed String: ",str1[::-1]) # Reversing the string
else:
	print("Length of String is not a multiple of 4")