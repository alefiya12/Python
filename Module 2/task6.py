# Write a Python function that takes a list and returns a new list with unique elements of the first list.
list1 = [5,9,6,7,3,5,5,9,4,7]
unique_list = []
for i in list1:
	if i not in unique_list:
		unique_list.append(i)
print("Original List:",list1)
print("List with Unique Elements:",unique_list)