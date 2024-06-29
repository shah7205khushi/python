# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:56:18 2024

@author: khush
"""

#Write a Python function to update a dictionary with key-value pairs from another
#dictionary.

def update_dictionary(dict1, dict2):
    dict1.update(dict2)

# Example usage:
dict1 = {'a': 1, 'b': 2,'e':22}
dict2 = {'b': 3, 'c': 4,'d':56}
update_dictionary(dict1, dict2)
print(dict1)  


#{'a': 1, 'b': 3, 'e': 22, 'c': 4, 'd': 56}