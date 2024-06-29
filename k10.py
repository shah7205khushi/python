# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:29:11 2024

@author: khush
"""

#10. Write a Python function to remove all whitespace characters from a given string.

def remove_whitespace(string):
    return string.replace(" ", "")

# Example usage:
input_string = input("Enter a string: ")
w = remove_whitespace(input_string)
print("String with whitespace removed:", w)

"""
Enter a string: k h u s h i
String with whitespace removed: khushi

"""
