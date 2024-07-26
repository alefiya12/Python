# Write a Python program to create a dictionary from a string.
# o Note: Track the count of the letters from the string.
# Sample string: 'w3resource'
# o Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
str1 = "w3resource"
print("String:",str1)
my_dict = {}
for i in str1:
	my_dict[i]=str1.count(i)
print("Output:",my_dict)