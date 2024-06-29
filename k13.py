# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:49:33 2024

@author: khush
"""

#Write a Python function to extract a sublist from a given list using slicing

def extract_sublist(lst, start, end):
    return lst[start:end]

# Example usage:
l = input("Enter elements of the list separated by spaces: ").split()
s = int(input("Enter the start index: "))
e = int(input("Enter the end index: "))
s = extract_sublist(l, s ,e)
print("Extracted sublist:", s)


"""
Enter elements of the list separated by spaces: 1 2 3 4 5 6 7 8 9
Enter the start index: 3 
Enter the end index: 7
Extracted sublist: ['4', '5', '6', '7']

"""
