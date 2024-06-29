# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:11:04 2024

@author: khush
"""

#38) Write a python program to display pyramid of horizontal tables

num= int(input("number"))

for i in range(0,num):
    for k in range(0,num-i-1):
        print(end=" ")
    for j in range(1,1+i):
        print(i*j,end=" ")
    print()

rows = int(input("Enter the number of rows: "))

"""

   1 
    2 4 
   3 6 9 
  4 8 12 16 
 5 10 15 20 25 
6 12 18 24 30 36

"""

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j * i, end=" ")
    print()
    
    
    """
    
    Enter the number of rows: 5
    1 
    2 4 
    3 6 9 
    4 8 12 16 
    5 10 15 20 25 
    
    """
