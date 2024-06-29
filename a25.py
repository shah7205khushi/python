# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:06:48 2024

@author: khush
"""

#25) Write a python program to display factors of a number

num = int(input("Enter a number: "))

print("Factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)



"""

Enter a number: 24
Factors of 24 are:
1
2
3
4
6
8
12
24

"""