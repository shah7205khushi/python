# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 23:08:03 2024

@author: khush
"""

# 23) Write a python program to check armstrong number. (eg. 13 + 33 + 53 = 153)
 
i = int(input("Enter a number: "))

temp=i
sum = 0

while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if temp==sum:
     print("number is Armstrong")
else:
     print("number is not Armstorng")
     
     
"""
output

Enter a number: 8
number is not Armstorng


Enter a number: 153
number is Armstrong

"""     