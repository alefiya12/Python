# Write a Python program to check whether a list contains a sub list
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = [4, 5, 6]
count=0
for i in sub_list:
    if i in main_list:
        count = count+1

if count==len(sub_list):
    print("The main list contains the sublist.")
else:
    print("The main list does not contain the sublist.")