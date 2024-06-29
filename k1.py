# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:25:59 2024

@author: khush
"""

#1.)Write a Python function to read and reverse a string

def reverse_string(string):
    reverse = ""
    for char in string:
        reverse = char + reverse
    return reverse


string = input("Enter a string: ")

reverse= reverse_string(string)

print("Reversed string:", reverse)

"""
Enter a string: khushi
Reversed string: ihsuhk

"""
