# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:16:56 2024

@author: khush
"""

#39) Write a python program to display pyramid pattern of alternate numbers

def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print the numbers in the row
        for j in range(1, i + 1):
            print(i * 2 - 1, end=" ")
        print()

rows = int(input("Enter the number of rows: "))
inverted_pyramid(rows)


"""
number8
7 7 7 7 
 5 5 5 
  3 3 
   1 

"""

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    num = 1
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 2
    print()
    
    """
    Enter the number of rows: 6
    1 
    1 3 
    1 3 5 
    1 3 5 7 
    1 3 5 7 9 
    1 3 5 7 9 11 
    """
