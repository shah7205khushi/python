# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:38:48 2024

@author: khush
"""

#11.)Write a Python function to extract even and odd indexed elements from a given list using slicing.

def extract_even_odd(lst):
    even = lst[::2]
    odd = lst[1::2]
    return even, odd

# Example usage:
lst = input("Enter elements of the list separated by spaces: ").split()
even, odd = extract_even_odd(lst)
print("Even indexed elements:", even)
print("Odd indexed elements:", odd)

"""
Enter elements of the list separated by spaces: 5 6 7 8 9 1 2 4 3
Even indexed elements: [5, 7, 9, 2, 3]
Odd indexed elements: [6, 8, 1, 4]

"""

