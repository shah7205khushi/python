# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:14:22 2024

@author: khush
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Main function with menu-driven approach
def main():
    print("Menu:")
    print("1. Calculate Area of Circle")
    print("2. Calculate Area of Rectangle")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            circle = Circle(radius)
            print(f"Area of the circle: {circle.calculate_area()}")
        elif choice == '2':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            rectangle = Rectangle(length, width)
            print(f"Area of the rectangle: {rectangle.calculate_area()}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()


"""
Menu:
1. Calculate Area of Circle
2. Calculate Area of Rectangle
3. Exit
Enter your choice (1/2/3): 1
Enter the radius of the circle: 7
Area of the circle: 153.93804002589985
Enter your choice (1/2/3): 2
Enter the length of the rectangle: 4
Enter the width of the rectangle: 5
Area of the rectangle: 20.0
Enter your choice (1/2/3): 
    
    """