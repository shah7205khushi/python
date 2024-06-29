# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 21:49:34 2024

@author: khush
"""

#. Create an interface Shape with methods area() and perimeter()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating instances of Rectangle and Circle
rectangle = Rectangle(4, 7)
circle = Circle(5)

# Displaying the area and perimeter of the shapes
print(f'Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}')
print(f'Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}')


"""

Rectangle - Area: 28, Perimeter: 22
Circle - Area: 78.5, Perimeter: 31.400000000000002

"""





"""




from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

# Creating instances of Rectangle, Circle, Square, and Triangle
rectangle = Rectangle(4, 7)
circle = Circle(5)
square = Square(6)
triangle = Triangle(3, 4, 5)

# Displaying the area and perimeter of the shapes
print(f'Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}')
print(f'Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}')
print(f'Square - Area: {square.area()}, Perimeter: {square.perimeter()}')
print(f'Triangle - Area: {triangle.area()}, Perimeter: {triangle.perimeter()}')



"""