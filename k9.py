# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:26:34 2024

@author: khush
"""

#9.)Write a Python function to swap the case of each character in a given string.

def swap_case(string):
    return string.swapcase()

# Example usage:
input_string = input("Enter a string: ")
swapped_string = swap_case(input_string)
print("Swapped case string:", swapped_string)


"""
Enter a string: KHUSHI
Swapped case string: khushi

Enter a string: khushi
Swapped case string: KHUSHI

Enter a string: KHUshi
Swapped case string: khuSHI

"""