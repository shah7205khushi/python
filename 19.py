# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:13:12 2024

@author: khush
"""

# Format - Strings

#The format() method takes the passed arguments, formats them, and places 
#them in the string where the placeholders {} are:
    
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#I want to pay 49.95 dollars for 3 pieces of item 567.
