# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:24:31 2024

@author: khush
"""

#40) Write a python program to display mirrored pyramid (right-angled triangle) pattern of numbers


rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    
    # Print numbers in each row
    for j in range(1, i + 1):
        print(j, end="")
    
    # Move to the next line
    print()
    
    
    """
    Enter the number of rows: 4
       1
      12
     123
    1234
    
    """
    
