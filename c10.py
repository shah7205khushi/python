# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:39:18 2024

@author: khush
"""

#Write a python program to handle the ZeroDivisionError exception

try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    
    result = dividend / divisor
    print("Result of division:", result)

except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")
 

"""
Enter the dividend: 6
Enter the divisor: 0
Error: Division by zero!

"""