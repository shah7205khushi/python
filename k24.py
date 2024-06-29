# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:54:31 2024

@author: khush
"""

#24. Write a Python function to generate a list of squares of numbers from 1 to N using list comprehension

def generate_squares(N):
    return [i*i for i in range(1, N+1)]

# Test the function
N = int(input("Enter the value of N: "))
s = generate_squares(N)
print("List of squares from 1 to", N, ":", s)

"""
Enter the value of N: 5
List of squares from 1 to 5 : [1, 4, 9, 16, 25]

"""


