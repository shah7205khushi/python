# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:32:12 2024

@author: khush
"""

#32) Write a python program to display reverse pyramid of numbers



def reverse_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print("", end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


rows = 5
reverse_pyramid(rows)

"""
1 2 3 4 5 
 1 2 3 4 
  1 2 3 
   1 2 
    1 
    """

"""

rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

    
    Enter the number of rows: 9
    1 2 3 4 5 6 7 8 9 
    1 2 3 4 5 6 7 8 
    1 2 3 4 5 6 7 
    1 2 3 4 5 6 
    1 2 3 4 5 
    1 2 3 4 
    1 2 3 
    1 2 
    1 
    
    """
