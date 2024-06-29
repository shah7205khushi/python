# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:09:12 2024

@author: khush
"""

#29) Write a python program to display inverted pyramid of numbers

"""
rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
"""

"""
Enter the number of rows: 5
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 

"""

def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(0, rows - i):
            print(" ", end="")
        for j in range(1, i):
            print(j, end=" ")
        print()


rows = 6
inverted_pyramid(rows)

"""
1 2 3 4 5 
 1 2 3 4 
  1 2 3 
   1 2 
    1 

"""