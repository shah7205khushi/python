# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:40:17 2024

@author: khush
"""

#5. Write a Python function to count the number of words in a given string

def count_words(string):
    words = string.split()
    return len(words)

input_string = input("Enter a string: ")
word_count = count_words(input_string)
print("Number of words:", word_count)

"""

Enter a string: khushi shah
Number of words: 2

"""
