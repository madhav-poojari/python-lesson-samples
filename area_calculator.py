import math

# Welcome message
print("Welcome to the Area Calculator!")

# Ask user for input
shape = input("Choose a shape to calculate the area (circle/rectangle/triangle): ")

# Process user's choice
if shape.lower() == 'circle':
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print("The area of the circle is:", area)
elif shape.lower() == 'rectangle':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is:", area)
elif shape.lower() == 'triangle':
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)
else:
    print("Invalid shape! Please choose circle, rectangle, or triangle.")

# End of the program
print("Thank you for using the Area Calculator!")
