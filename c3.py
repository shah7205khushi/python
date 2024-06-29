# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:29:36 2024

@author: khush
"""

"""
Define class Surface_Area which includes three methods with the name Calculate_area() 
(Function Overloading). Each method accepts parameter(s) to calculate area of circle, 
rectangle and triangle. Display the result from calling of respective Calculate_area() as per 
the user’s request. Design the menu-driven program.

"""
class Surface_Area:
    def calculate_area(self, radius=None, length=None, width=None, height=None, base=None):
        if radius is not None:
            return self.calculate_area_circle(radius)
        elif length is not None and width is not None:
            return self.calculate_area_rectangle(length, width)
        elif height is not None and base is not None:
            return self.calculate_area_triangle(height, base)
        else:
            print("Invalid input")

    def calculate_area_circle(self, radius):
        return 3.14 * radius * radius

    def calculate_area_rectangle(self, length, width):
        return length * width

    def calculate_area_triangle(self, height, base):
        return 0.5 * height * base

surface_area = Surface_Area()

while True:
    print("1. Calculate area of Circle")
    print("2. Calculate area of Rectangle")
    print("3. Calculate area of Triangle")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        print("Area of the circle:", surface_area.calculate_area(radius=radius))
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("Area of the rectangle:", surface_area.calculate_area(length=length, width=width))
    elif choice == 3:
        height = float(input("Enter the height of the triangle: "))
        base = float(input("Enter the base of the triangle: "))
        print("Area of the triangle:", surface_area.calculate_area(height=height, base=base))
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")



"""
1. Calculate area of Circle
2. Calculate area of Rectangle
3. Calculate area of Triangle
4. Exit
Enter your choice: 1
Enter the radius of the circle: 3
Area of the circle: 28.259999999999998
1. Calculate area of Circle
2. Calculate area of Rectangle
3. Calculate area of Triangle
4. Exit
Enter your choice: 2
Enter the length of the rectangle: 6
Enter the width of the rectangle: 4
Area of the rectangle: 24.0
1. Calculate area of Circle
2. Calculate area of Rectangle
3. Calculate area of Triangle
4. Exit
Enter your choice: 3
Enter the height of the triangle: 6
Enter the base of the triangle: 4
Area of the triangle: 12.0
1. Calculate area of Circle
2. Calculate area of Rectangle
3. Calculate area of Triangle
4. Exit
Enter your choice: 4
Exiting...


"""