# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:11:00 2024

@author: khush
"""

#7. Write a Python function to convert the first letter of each word to uppercase in a given string.


def capitalize_first_letter(string):
    words = string.split()
    result = ''
    for word in words:
        capital = word.capitalize()
        result += capital + ' '
    return result


input_string = input("Enter a string: ")
capitalstr= capitalize_first_letter(input_string)
print("Capitalized string:", capitalstr)

"""
Enter a string: khushi
Capitalized string: Khushi
"""
