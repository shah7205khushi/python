# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:20:40 2024

@author: khush
"""

#Write a Python function to count the frequency of a substring within a string.

def count_substring(string, substring):
    count = string.count(substring)
    return count


istr = input("Enter a string: ")
substr = input("Enter a substring to count: ")
frequency = count_substring(istr, substr)
print("Frequency of substring:", frequency)

"""
Enter a string: hello i am khushi . i live in ahmedabad
Enter a substring to count: i
Frequency of substring: 5

"""