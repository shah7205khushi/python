# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:57:27 2024

@author: khush
"""

#36) Write a python program to display connected inverted pyramid pattern of numbers

num= int(input("number"))

for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
    
    """
     1
    212
   32123
  4321234
 543212345
65432123456

"""

rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for k in range(2, i + 1):
        print(k, end="")
    print()


"""
Enter the number of rows: 5
543212345
 4321234 
  32123
   212
    1


"""