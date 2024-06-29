# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:48:57 2024

@author: khush
"""

#Write a Python function to get all keys from a dictionary.

"""

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

for key in my_dict:
 print(key) 
 
 """
 
 
def keys(d):
    return d.keys()

# Example usage:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
keys = keys(my_dict)
print(keys) 

 # Output: dict_keys(['name', 'age', 'city'])
