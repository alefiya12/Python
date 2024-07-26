# Write a Python program to find the repeated items of a tuple.
tuple1 = ("a", "f", "e", "d", "a", "c", "a", "e", "a", "c")
list1 = []
print("Tuple:",tuple1,"\n")
for i in tuple1:
	if i not in list1:
		if tuple1.count(i)>1:
			print(f"{i} is repeated {tuple1.count(i)} times in Tuple.")
			list1.append(i)