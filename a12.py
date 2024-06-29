# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 11:44:57 2024

@author: khush
"""


number = int(input("Enter a number to generate its multiplication table: "))


print("Multiplication table for:",number)
for i in range(1, 11):
    print(number, 'x', i, '=', number * i)
    
"""
    output
    
    Enter a number to generate its multiplication table: 8
    Multiplication table for 8:
    8 x 1 = 8
    8 x 2 = 16
    8 x 3 = 24
    8 x 4 = 32
    8 x 5 = 40
    8 x 6 = 48
    8 x 7 = 56
    8 x 8 = 64
    8 x 9 = 72
    8 x 10 = 80

"""