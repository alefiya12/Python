# Write a Python function that checks whether a passed string is palindrome or not
str1 = "ava"
str1 = str1.upper()
str2 = str1[::-1]
if str1==str2:
    print(str1,"is Palindrome")
else:
    print(str1,"is not Palindrome")