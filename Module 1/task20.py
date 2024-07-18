# Write a Python function to insert a string in the middle of a string.
def insert_middle(main_str,insert_str):
	center = len(main_str)//2 # Finding Center of string
	result = main_str[:center]+insert_str+main_str[center:]
	print("Result: ",result)

main_str = input("Enter Main String: ") # User Input
insert_str = input("Enter Insert String: ") # User Input
insert_middle(main_str,insert_str) # Calling Function