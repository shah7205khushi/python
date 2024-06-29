# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:40:04 2024

@author: khush
"""

#43) Write a python program to display pyramid pattern of stars


rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
    
    """
    Enter the number of rows: 8
           *
          ***
         *****
        *******
       *********
      ***********
     *************
    ***************
    
    """
