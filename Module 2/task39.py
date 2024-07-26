# Write a Python program to returns sum of all divisors of a number
number = int(input("Enter a number: "))

sum_of_divisors = 0

for i in range(1, number + 1):
    if number % i == 0: 
        sum_of_divisors += i
print("Sum of all divisors:", sum_of_divisors)