# Write a Python program to remove an empty tuple(s) from a list of tuples.
list_of_tuples = [(1, 2, 3), (), (4, 5, 6), (7, 8, 9), ()]
print(list_of_tuples)
for i in list_of_tuples:
	if len(i)==0:
		list_of_tuples.remove(i)

print(list_of_tuples)