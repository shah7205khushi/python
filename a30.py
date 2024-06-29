# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:18:26 2024

@author: khush
"""

#30) Write a python program to display inverted pyramid of descending numbers


def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(0, rows - i):
            print(" ", end="")
        for j in range(i, 0, -1):  # Adjusted to run from i down to 1
            print(j, end=" ")      # Printing numbers in descending order
        print()


rows = 6
inverted_pyramid(rows)

"""

6 5 4 3 2 1 
 5 4 3 2 1 
  4 3 2 1 
   3 2 1 
    2 1 
     1 
     
     """



"""
rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()




Enter the number of rows: 5
5 4 3 2 1 
  4 3 2 1 
    3 2 1 
      2 1 
        1 
        
        """