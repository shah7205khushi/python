# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:50:52 2024

@author: khush
"""

#22. Write a Python function to remove duplicates from a list.

def remove_duplicates(lst):
    return list(set(lst))

input_list = [int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]
result = remove_duplicates(input_list)
print("List after removing duplicates:", result)

"""
Enter the list of numbers separated by spaces: 1 2 3 4 5 1 2 
List after removing duplicates: [1, 2, 3, 4, 5]

"""
