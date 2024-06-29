# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 23:24:13 2024

@author: khush
"""

#26) Write a python programs to create pyramid and pattern.


rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end=" ")
    print("\n")
    
    
"""
output

Enter number of rows: 5
* 

* * 

* * * 

* * * * 

* * * * * 

"""    

num = int(input("enter num"))

for i in range(0,num):
    for j in range(0,num-1-i):
        print(end=" ")
    for j in range(0,i+1):
        print("*" ,end=" ")
    print()


"""
enter num9
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
  * * * * * * * 
 * * * * * * * * 
* * * * * * * * * 

"""