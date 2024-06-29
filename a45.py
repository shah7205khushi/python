# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:50:18 2024

@author: khush
"""

#45) Write a python program to display pascal’s triangle program

rows = int(input("Enter the number of rows for Pascal's triangle: "))

for i in range(rows):
    num = 1
    for j in range(1, rows - i):
        print("  ", end="")
    
    for k in range(0, i + 1):
        print("  ", num, sep="", end="")
        num = num * (i - k) // (k + 1)
    
    print()

"""
Enter the number of rows for Pascal's triangle: 7
              1
            1  1
          1  2  1
        1  3  3  1
      1  4  6  4  1
    1  5  10  10  5  1
  1  6  15  20  15  6  1
  
  """
  
