# Write python program that user to enter only odd numbers, else will raise an exception.
class EvenNumberError(Exception): # Initializing Error
	pass

while True:
	try: # Try Block
		n = int(input("Enter Odd Numbers only: ")) 
		if n % 2 == 0:
			raise EvenNumberError("You entered an even number!")
	except EvenNumberError as e: # Except Block
		print(e)
		break