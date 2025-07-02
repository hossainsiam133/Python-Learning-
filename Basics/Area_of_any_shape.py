##import math
from my_std_imports import*
## Triangle
base = float(input("Enter the Base: "))
height = float(input("Enter the Height: "))
triangle_area = 1 / 2 * base * height
print("Area of Triangle: %.2f" % triangle_area)
## Circle
radius = float(input("Enter the Radius: "))
cicle_area = math.pi * (radius**2)
print("Area of Circle: %.2f" % cicle_area)
