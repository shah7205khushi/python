# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:46:29 2024

@author: khush
"""


#6. Write a Python function to convert a CamelCase string to snake_case.

def camel_to_snake(s):
    result = ""
    
    for char in s:
        if char.isupper():
            result += '_' + char.lower()
        else:
            result += char
    
    if result.startswith('_'):
        result = result[1:]
    
    return result

# Example usage:
print(camel_to_snake("CamelCaseString"))  # camel_case_string
print(camel_to_snake("ThisIsATest"))  # this_is_a_test
print(camel_to_snake("camelCase"))  # camel_case
