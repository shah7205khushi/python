# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:53:20 2024

@author: khush
"""

#Write a Python function to compute the factorial of a given number recursively

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of", num, "is", result)

"""
Enter a number: 5
Factorial of 5 is 120

"""