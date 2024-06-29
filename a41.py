# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:28:55 2024

@author: khush
"""

#41) Write a python program to display equilateral triangle with stars (asterisk symbol)

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

"""
Enter the number of rows: 6
     *
    ***
   *****
  *******
 *********
***********

"""
n = int(input("number:"))
k=2
for i in range(1,n+1):
    for j in range(1,n*2):
        if( i==n or i+j==n+1 or j-i== n-1):
            print("*" ,end="")         
        else:
            print(end=" ")
    print()
