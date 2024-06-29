# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:32:30 2024

@author: khush
"""

#42) Write a python program to display downward triangle pattern of stars

rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    print("*" * (2 * i - 1))


"""
Enter the number of rows: 7
*************
***********
*********
*******
*****
***
*

"""