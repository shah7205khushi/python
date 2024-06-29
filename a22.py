# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 22:58:26 2024

@author: khush
"""

#22) Write a python program to display prime numbers between two intervals.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Print prime numbers between 1 and 100
for number in range(1, 101):
    if is_prime(number):
        print(number, end=' ')



"""



start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print("Prime numbers between", start, "and", end, "are:")


for num in range(start, end + 1):
    
    if num < 2:
        continue

    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num)

output

Enter the start of the interval: 1
Enter the end of the interval: 10
Prime numbers between 1 and 10 are:
2
3
5
7

"""