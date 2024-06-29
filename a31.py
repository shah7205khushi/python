# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:23:27 2024

@author: khush
"""

#31) Write a python program to display inverted pyramid of the same digit



def inverted_same_digit_pyramid(rows, digit):
    for i in range(rows, 0, -1):
        for j in range(0, rows - i):
            print(" ", end="")
        for j in range(0, i):
            print(digit, end=" ")
        print()


rows = 5
digit = 7
inverted_same_digit_pyramid(rows, digit)

"""

def inverted_same_digit_pyramid(rows, digit):
    for i in range(rows, 0, -1):
        for j in range(0, rows - i):
            print(" ", end="")
        for j in range(0, i):
            print(digit, end=" ")
        print()


rows = 5
digit = 7
inverted_same_digit_pyramid(rows, digit)

"""

"""

rows = int(input("Enter the number of rows: "))
digit = int(input("Enter the digit: "))

for i in range(rows, 0, -1):
    for j in range(i):
        print(digit, end=" ")
    print()




Enter the number of rows: 8
Enter the digit: 5
55555555
5555555
555555
55555
5555
555
55
5

"""


