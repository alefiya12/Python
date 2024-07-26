# Write a Python script to check if a given key already exists in a dictionary.
dict1 = {"a" : 1, "b" : 2, "c" : 3}
key = "a"
if key in dict1.keys():
	print("Key exists in the Dictionary")
else:
	print("Key does not exists in the Dictionary")