# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:22:22 2024

@author: khush
"""

#18) Write a python program to find binary value of a character.


character = input("Enter a character: ")

binary_value = bin(ord(character))[2:]

print("Binary value of", character, "is:", binary_value)
