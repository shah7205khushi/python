# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:25:41 2024

@author: khush
"""

# 7) Write a python program to find largest number among three numbers.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


if num1 >= num2 and num1 >= num3:
    largest_number = num1
elif num2 >= num1 and num2 >= num3:
    largest_number = num2
else:
    largest_number = num3

print("The largest number is:", largest_number)

"""
output

Enter the first number: 998
Enter the second number: 5677
Enter the third number: 98765
The largest number is: 98765
"""