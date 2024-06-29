# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:01:46 2024

@author: khush
"""

#18. Write a Python function to check if a given number is prime or not prime.

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
