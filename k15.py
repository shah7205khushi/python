# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:00:51 2024

@author: khush
"""

#15. Write a Python function to replace a sublist within a list with another sublist using slicing.

def replace_sublist(lst, start, end, replace):
    lst[start:end] = replace


i = input("Enter elements of the list separated by spaces: ").split()
s = int(input("Enter the start index of the sublist to replace: "))
e= int(input("Enter the end index of the sublist to replace: "))
r= input("Enter elements of the replacement sublist separated by spaces: ").split()
replace_sublist(i, s, e, r)
print("Updated list:", i)

"""
Enter elements of the list separated by spaces: 1 2 3 4 5 6 
Enter the start index of the sublist to replace: 1
Enter the end index of the sublist to replace: 3
Enter elements of the replacement sublist separated by spaces: 7 8 9
Updated list: ['1', '7', '8', '9', '4', '5', '6']

"""