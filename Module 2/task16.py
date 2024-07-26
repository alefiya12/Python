# Write a Python program to replace last value of tuples in a list.
list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 11

print("Original list of tuples:", list_of_tuples)
updated_list = [t[:-1] + (new_value,) for t in list_of_tuples] # Concatenating one tuple to another
print("Updated list of tuples:", updated_list)