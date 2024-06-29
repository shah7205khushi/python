# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:01:09 2024

@author: khush
"""

#4) Write a python program to read two numbers and display the greatest number.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


greatest_number = max(num1, num2)


print("The greatest number is:", greatest_number)

"""
output

Enter the first number: 78
Enter the second number: 98
The greatest number is: 98
"""