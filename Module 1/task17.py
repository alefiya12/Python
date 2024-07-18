# Write a Python function that takes a list of words and returns the length of the longest one.
lst1 = ["Apple","Watermelon","Cherry"] # List of words
length = 0
for i in lst1:
	if len(i)>length: # Checking Length
		longest = i
		length = len(i)
print("Longest Word in the List is: ",longest)