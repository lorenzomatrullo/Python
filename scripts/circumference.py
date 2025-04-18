import math

radius = float(input("Whats the radius of the circle?: "))

circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")

# Calculate the area of a circle
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm²")