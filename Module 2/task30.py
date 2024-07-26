# Write a Python program to find the highest 3 values in a dictionary
dict1 = {'a':1, 'b':5, 'c':3, 'd':8, 'e':7, 'f':2, 'g':4, 'h':6, 'i':9}
sorted_dict = sorted(dict1.values())
print("Highest 3 Values are:",sorted_dict[-3:])