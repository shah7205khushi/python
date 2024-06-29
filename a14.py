# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:06:02 2024

@author: khush
"""

# 14) Write a python program to find gcd.


a=int(input("enter first num :"))
b=int(input("enter second num:"))


while a%b!=0 :
    rem=a%b
    a=b
    b=rem
   
print("GCD is ", rem)

"""
enter first num :16
enter second num12
GCD is  4

"""