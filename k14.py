# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:56:32 2024

@author: khush
"""

#14. Write a Python function to extract alternate elements from a given list using slicing

def alternate_ele(lst):
    return lst[::2]


input_list = input("Enter elements of the list separated by spaces: ").split()
a= alternate_ele(input_list)
print("Alternate elements:", a)

"""

Enter elements of the list separated by spaces: 3 5 6 8 3 2 9
Alternate elements: ['3', '6', '3', '9']

Enter elements of the list separated by spaces: K H U S H I
Alternate elements: ['K', 'U', 'H']

"""