# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:45:59 2024

@author: khush
"""

#11.)Write a Python function to reverse a given list using slicing.

def reverse_list(lst):
    return lst[::-1]


input_list = input("Enter elements of the list separated by spaces: ").split()
r = reverse_list(input_list)
print("Reversed list:", r)

"""

Enter elements of the list separated by spaces: 9 8 7 6 5 4 3 2 1
Reversed list: ['1', '2', '3', '4', '5', '6', '7', '8', '9']

"""