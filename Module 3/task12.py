# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangle: # Class Rectangle
	def __init__(self,length,width): # Constructor
		self.length=length
		self.width=width

	def calculate_area(self): # Calculating Area
		area=self.length * self.width
		print("Area of Rectangle:",area)

length=int(input("Enter Length of Rectangle: "))
width=int(input("Enter Width of Rectangle: "))

rec1=Rectangle(length,width)
rec1.calculate_area()