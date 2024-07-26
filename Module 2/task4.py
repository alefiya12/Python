# Write a Python function that takes two lists and returns true if they have at least one common member.
list1 = ["A", "B", "C", "D"]
list2 = ["D", "E", "F", "G"]
for i in list1:
	if i in list2:
		print("True")
		break
