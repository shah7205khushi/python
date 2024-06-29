# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:43:48 2024

@author: khush
"""

#34) Write a python program to display pyramid of natural numbers less than 10



for i in range(1, 10):
    print(" " * (10 - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for k in range(i - 1, 0, -1):
        print(k, end=" ")
    print()
    
    
"""
    for i in range(1, 10):
    print(" " * (9 - i), end="")
    print(*range(1, i), *range(i, 0, -1))
"""


"""
        1
       1 2 1
      1 2 3 2 1
     1 2 3 4 3 2 1
    1 2 3 4 5 4 3 2 1
   1 2 3 4 5 6 5 4 3 2 1
  1 2 3 4 5 6 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

"""
