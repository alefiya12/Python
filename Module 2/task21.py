# Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'apple': 10, 'banana': 2, 'cherry': 7, 'date': 5}
asecding = sorted(my_dict.items(), key=lambda item: item[1])
descending = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
print(asecding)
print(descending)