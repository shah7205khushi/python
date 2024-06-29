# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:52:51 2024

@author: khush
"""

#35) Write a python program to display reverse pattern of digits from 10




for i in range(10, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


"""
10 9 8 7 6 5 4 3 2 1 
9 8 7 6 5 4 3 2 1 
8 7 6 5 4 3 2 1 
7 6 5 4 3 2 1 
6 5 4 3 2 1 
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 

"""
