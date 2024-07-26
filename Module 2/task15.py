# Write a Python program to find the length of a tuple.
tuple1 = (1,2,3,4,5,6,7,8,9)
print("Tuple:",tuple1)
print("Length of Tuple: ",len(tuple1))

# Write a Python program to convert a list to a tuple.
list1 = [5,9,6,7,3,5,5,9,4,7]
print("\nList:",list1)
print(type(list1))
list1 = tuple(list1)
print("Tuple:",list1)
print(type(list1))

# Write a Python program to reverse a tuple.
print("\nOriginal Tuple:",tuple1)
print("Reversed Tuple: ",tuple1[::-1])