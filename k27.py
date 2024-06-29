# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:38:29 2024

@author: khush
"""

#Write a Python function to access the value associated with a given key in a dictionary.

"""

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
a= my_dict["age"]
print(a) 

"""

def get_value(d, key):
    return d[key]

# Example usage:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
age = get_value(my_dict, "age")
print(age)  # Output: 30
