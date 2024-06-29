# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:21:44 2024

@author: khush
"""

#Write a Python function to merge two dictionaries.

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of the first dictionary
    merged_dict.update(dict2)   # Update it with the second dictionary
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dictionaries(dict1, dict2))  # Output: {'a': 1, 'b': 3, 'c': 4}
