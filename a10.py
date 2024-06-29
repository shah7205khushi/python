# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:51:53 2024

@author: khush
"""

# 10) Write a python program to check leap year.


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
    
"""
output

Enter a year: 1976
1976 is a leap year.


Enter a year: 1966
1966 is not a leap year.

"""