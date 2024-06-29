# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:12:16 2024

@author: khush
"""

#13)Write a python program to display fibonacci series.

num = int(input("enter number :"))

n1=0
n2=1
sum=0

if num<=0:
    print("please enter the number greater than 0")
else:
    for i in range(0,num):
        print (sum,end= " ")
        n1=n2              
        n2=sum
        sum=n1+n2
       
        
#output

"""
enter number :7
0 1 1 2 3 5 8   
     
"""        
        