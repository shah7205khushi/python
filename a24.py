# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:50:02 2024

@author: khush
"""

#24.)Write a python program to display armstrong number between two intervals.


def is_armstrong(num):
    temp = num
    sum = 0
    while num > 0:
        sum = sum + (num % 10) * (num % 10) * (num % 10)
        num = num // 10
    return temp == sum

# Print Armstrong numbers between 1 and 100
for number in range(1, 500):
    if is_armstrong(number):
        print(number, end=' ')




"""


start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

print("Armstrong numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3  # Cube of each digit
        temp //= 10
    if num == sum:
        print(num)
        
        
Enter the starting number of the interval: 1
Enter the ending number of the interval: 500
Armstrong numbers between 1 and 500 are:
1
153
370
371
407

"""