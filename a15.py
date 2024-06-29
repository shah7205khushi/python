# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:16:34 2024

@author: khush
"""

#15) Write a python program to find lcm

def lcm(x, y):
    max_num = max(x, y)
    
    while(True):
        if max_num % x == 0 and max_num % y == 0:
            return max_num
        
        max_num += max(x, y)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = lcm(num1, num2)


print("LCM of", num1, "and", num2, "is:", result)

"""
Enter first number: 4
Enter second number: 8
LCM of 4 and 8 is: 8

"""
