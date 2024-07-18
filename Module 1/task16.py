# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string.
sentence = input("Enter a string: ") # User Input

# Finding Index
not_index = sentence.find('not')
poor_index = sentence.find('poor')

if not_index != -1 and poor_index != -1 and not_index < poor_index:
    # Replace 'not'...'poor' with 'good'
    sentence = sentence[:not_index] + 'good' + sentence[poor_index + 4:]

print("Result: ",sentence)