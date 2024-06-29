# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:44:17 2024

@author: khush
"""

#21. Write a Python function to calculate the sum of all elements in a list.

def sum_of_elements(lst):
    return sum(lst)

numbers = [int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]
result = sum_of_elements(numbers)
print("Sum of all elements in the list:", result)

"""
Enter the list of numbers separated by spaces: 4 3 5 1 6 7
Sum of all elements in the list: 26

"""