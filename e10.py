# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:38:51 2024

@author: khush
"""

from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height, co_eff=0.5):
        self.base = base
        self.height = height
        self.co_eff = co_eff

    def calculate_area(self):
        return self.co_eff * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

def main():
    while True:
        print("\nMenu")
        print("1. Calculate area of Triangle")
        print("2. Calculate area of Rectangle")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            triangle = Triangle(base, height)
            print(f"The area of the triangle is: {triangle.calculate_area()}")

        elif choice == '2':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            rectangle = Rectangle(length, width)
            print(f"The area of the rectangle is: {rectangle.calculate_area()}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()
