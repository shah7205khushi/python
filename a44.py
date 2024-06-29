# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:47:35 2024

@author: khush
"""

#44) Write a python program to display hourglass pattern program

rows = int(input("Enter the number of rows: "))

# Upper half of the hourglass
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Lower half of the hourglass
for i in range(2, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


"""
Enter the number of rows: 5
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********

"""
