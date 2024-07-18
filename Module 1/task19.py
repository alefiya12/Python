# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# o Sample String: w3resource' 
# o Expected Result: 'w3ce' 
# o Sample String: 'w3' 
# o Expected Result: 'w3w3' 
# o Sample String: ' w' 
# o Expected Result: Empty String

str = input("Enter a String: ") # User Input

if len(str)<2: # Checking Length of string
	print("Result: Empty String")
elif len(str)==2:
	str1 = str + str
	print("Result: ",str1)
else:
	str1 = str[:2] + str[len(str)-2:]
	print("Result: ",str1)