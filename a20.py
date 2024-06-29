# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:02:32 2024

@author: khush
"""

# 20) Write a python program to check whether a number is palindrome or not.



i=int(input("Enter Number:"))
rev=0
x=i

while(i>0):
        rev=(rev*10)+i%10
        i=i//10
if(x==rev):
    print("Palindrome Number")

else:
    print("Not Palindrome Number")
    
"""    
    
output

Enter Number:121
Palindrome Number 

Enter Number:538
Not Palindrome Number   

"""
       