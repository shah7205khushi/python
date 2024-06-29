# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:35:02 2024

@author: khush
"""

#9) Write a python program to calculate sum of natural numbers.

n = int(input("Enter a positive integer: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("The sum of natural numbers up to", n, "is:", sum)

"""
output

Enter a positive integer: 6
The sum of natural numbers up to 6 is: 21

"""
