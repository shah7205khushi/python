# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:32:24 2024

@author: khush
"""

#20. Write a Python function to convert temperature from Celsius to Fahrenheit and vice versa.

def c_to_f(c):
    f = (c * 9/5) + 32
    return f

def f_to_c(f):
    c = (f - 32) * 5/9
    return c

celsius = float(input("Enter temperature in Celsius: "))
fa = c_to_f(celsius)
print("Temperature in Fahrenheit:", fa)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
cel = f_to_c(fahrenheit)
print("Temperature in Celsius:",cel)

"""

Enter temperature in Celsius: 35
Temperature in Fahrenheit: 95.0
Enter temperature in Fahrenheit: 95
Temperature in Celsius: 35.0

"""