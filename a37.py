# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:04:06 2024

@author: khush
"""

#37) Write a python program to display even number pyramid pattern

num= int(input("number"))

for i in range(0,num):
    for j in range(0,num-1-i):
        print(end=" ")
    for k in range(0,i+1):
        print(i*2 ,end=" ")
    print()
    
    """
    0 
   2 2 
  4 4 4 
 6 6 6 6 
8 8 8 8 8 

"""


rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(2, i * 2 + 1, 2):
        print(j, end="")
    for k in range(i * 2 - 2, 0, -2):
        print(k, end="")
    print()

"""
Enter the number of rows: 4
   2
  242
 24642
2468642

"""