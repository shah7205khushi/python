# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:57:31 2024

@author: khush
"""

#17. Write a Python function to generate multiplication table of given number by the user

def multiplication_table(num):
    print("Multiplication table of", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

number = int(input("Enter a number: "))

multiplication_table(number)

"""
Enter a number: 7
Multiplication table of 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

"""