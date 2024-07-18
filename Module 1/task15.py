# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.
word = input("Enter a string: ") # User Input
if len(word) <= 3: # Checking Length
    print("Result:", word)
elif word.endswith('ing'):
    print("Result:", word + 'ly')
else:
	print("Result:", word + 'ing')