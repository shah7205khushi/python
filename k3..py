# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:53:09 2024

@author: khush
"""

#3. Write a Python function to remove duplicate characters from a string

def remove_duplicates(string):
    ustr = ''
    
    for char in string:
      
        if char not in ustr:
            ustr += char
    return ustr

# Example usage:
input_string = input("Enter a string: ")
result = remove_duplicates(input_string)
print("String after removing duplicates:", result)


"""
Enter a string: khushiiii
String after removing duplicates: khusi

"""