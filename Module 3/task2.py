# Write a Python program to append text to a file and display the text.
file = open("example.txt","a") # Open file in append mode
file.write("\nAppended Text in the example file.") # Writing in the file
file.close() # Close File
print("Text Appended to file example.txt")