# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
squares = [i*i for i in range(1, 31)]
print("First and last 5 elements of the list of squares between 1 and 30:", squares[:5] + squares[-5:])