# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:39:30 2024

@author: khush
"""

#21)Write a python program to check whether a number is prime or not.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")




"""


dnumber = int(input("Enter a number: "))


if number < 2:
    print(number, "is not a prime number.")
else:
    is_prime = True
    
    
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")




output

Enter a number: 7
7 is a prime number.

Enter a number: 98
98 is not a prime number.

"""



