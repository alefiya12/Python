# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
class Circle: # Class Rectangle
	def __init__(self,radius): # Constructor
		self.radius=radius
		self.pi=3.14
	def calculate_area(self): # Calculating Area
		area=self.pi*self.radius*self.radius
		print("Area of Circle:",area)

	def calculate_perimeter(self): # Calculating Perimeter
		perimeter=2*self.pi*self.radius
		print("Perimeter of Circle:",perimeter)

radius=int(input("Enter Radius of Rectangle: "))

circle1=Circle(radius)
circle1.calculate_area()
circle1.calculate_perimeter()