# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 12:19:04 2024

@author: khush
"""

#16) Write a python program to reverse a number.

number = int(input("Enter a number: "))

reverse = 0
original_number = number

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number =number // 10

print("The reverse of", original_number, "is:", reverse)

"""
output

Enter a number: 86437
The reverse of 86437 is: 73468

"""
