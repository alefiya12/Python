# Write a python program to find the longest words.
str1 = "What a Beautiful Day!"
words = str1.split()

# Find the maximum length of any word
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]

print("The longest words are:", longest_words)