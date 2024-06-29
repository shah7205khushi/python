# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:37:43 2024

@author: khush
"""

#33) Write a python program to display inverted half pyramid number pattern


def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        # Print leading spaces
        for j in range(rows - i):
            print("", end=" ")
        # Print numbers in the row
        for j in range(1, i + 1):
            print(j, end=" ")
        # Print numbers in reverse order except the last one to avoid duplicate
        
        print()

rows = 5
inverted_pyramid(rows)

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
    for j in range(i):
        print(i, end=" ")
    print()



Enter the number of rows: 5
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 

"""