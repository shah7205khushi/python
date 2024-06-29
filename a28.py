# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 09:43:42 2024

@author: khush
"""

#28) Write a python program to display Simple Number Triangle Pattern


rows = int(input("Enter the number of rows: "))


for i in range(1, rows + 1):
    
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
    
"""

Enter the number of rows: 8
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 

"""    
