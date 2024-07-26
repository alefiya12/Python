# Write a Python program to check multiple keys exists in a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = {'a', 'b'}
print("Does Keys exists in the Dictionary?",keys.issubset(my_dict))
