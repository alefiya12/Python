# Write python program that swap two number with temp variable and without temp variable.
num1 = int(input("Enter Number 1: ")) # User Input
num2 = int(input("Enter Number 2: ")) # User Input
a = num1
b = num2

print("\nWith 3rd Variable\nBEFORE SWAPPING\nNum 1:",num1,"Num 2:",num2,"\n") #Swapping with 3rd Variable
temp=num1
num1=num2
num2=temp
print("AFTER SWAPPING\nNum 1:",num1,"Num 2:",num2)

print("\nWithout 3rd Variable\nBEFORE SWAPPING\nNum 1:",a,"Num 2:",b,"\n") # Swapping without 3rd VAriable
a=a+b
b=a-b
a=a-b
print("AFTER SWAPPING\nNum 1:",a,"Num 2:",b)