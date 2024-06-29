# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:06:03 2024

@author: khush
"""

# 11) Write a python program to find factorial.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a  integer: "))

if number < 0:
    print("Factorial is not possible for negative numbers.")
else:
    print("Factorial of", number, "is:", factorial(number))
    
"""
output

Enter a  integer: 6
Factorial of 6 is: 720

"""    
    