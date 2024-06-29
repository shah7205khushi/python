# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:14:02 2024

@author: khush
"""

#6) Write a python program to check whether a character is vowel or consonant.

character = input("Enter a character: ")

if character in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
    print("The character is a vowel.")
else:
    print("The character is a consonant.")


"""
output

Enter a character: A
The character is a vowel.

Enter a character: N
The character is a consonant.

Enter a character: a
The character is a vowel.

Enter a character: h
The character is a consonant.

"""