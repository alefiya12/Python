# Write a Python program to split a list into different variables.
list1 = [1, 2, 3, 4, 5, 6, 7]

# Unpacking the list into variables with remaining elements collected into a list
a, b, c, d, e, *f = list1

print("a:", a)
print("b:", b)
print("c:", c)
print("a:", d)
print("b:", e)
print("c:", f)