# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:19:38 2024

@author: khush
"""

#Write a python program to overload the multiplication (*) operator that can act on objects 
#of NUM class having two members as no1 and no2.(with exception handling)

class NUM:
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2
    
    def __mul__(self, other):
        # Define the behavior of the * operator for NUM objects
        return NUM(self.no1 * other.no1, self.no2 * other.no2)
    
    def __add__(self, other):
        # Define the behavior of the + operator for NUM objects
        return NUM(self.no1 + other.no1, self.no2 + other.no2)
    
    def __sub__(self, other):
        # Define the behavior of the - operator for NUM objects
        return NUM(self.no1 - other.no1, self.no2 - other.no2)
    
    def __truediv__(self, other):
        # Define the behavior of the / operator for NUM objects
        if other.no1 == 0 or other.no2 == 0:
            raise ValueError("Cannot divide by zero")
        return NUM(self.no1 / other.no1, self.no2 / other.no2)
    
    def __mod__(self, other):
        # Define the behavior of the % operator for NUM objects
        if other.no1 == 0 or other.no2 == 0:
            raise ValueError("Cannot modulo by zero")
        return NUM(self.no1 % other.no1, self.no2 % other.no2)

    def __str__(self):
        return f'NUM(no1={self.no1}, no2={self.no2})'


# Creating instances of NUM class
num1 = NUM(10, 20)
num2 = NUM(2, 5)

# Performing various operations
result_mul = num1 * num2
result_add = num1 + num2
result_sub = num1 - num2
result_div = num1 / num2
result_mod = num1 % num2

# Displaying the results
print("Multiplication:", result_mul)
print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Division:", result_div)
print("Modulo:", result_mod)
