# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:43:54 2024

@author: khush
"""


#2.)Write a Python function to count the number of vowels in a given string

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))

"""
Enter a string: khushi
Number of vowels: 2

"""
