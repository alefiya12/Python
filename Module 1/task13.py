# Write a Python program to count the occurrences of each word in a given sentence
str1 = input("Enter a String: ") # User Input
str1=str1.lower()
word_count = {}
for i in str1: # Counting ocurences of each word in the sentence
	if i in word_count:
		word_count[i] += 1
	else:
		word_count[i] = 1
print("Word Occurences: ",word_count)