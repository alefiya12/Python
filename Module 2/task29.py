# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# o Sample data: {'1': ['a','b'], '2': ['c','d']} 
# o Expected Output: ac ad bc bd
d1 = {'1': ['a','b'], '2': ['c','d']} 
a, b = d1.values()
print(d1)
for i in a:
	for j in b:
		print(f"{i}{j}",end=" ")
print()