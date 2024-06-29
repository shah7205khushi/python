# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:59:57 2024

@author: khush
"""

#Modify Strings

a = "Hello, World!"
print(a.upper())

#HELLO, WORLD!

a = "Hello, World!"
print(a.lower())

#hello, world!

#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) 

# returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

#Jello, World!

#The split() method splits the string into substrings if it finds instances
# of the separator:

a = "Hello, World!"
print(a.split(",")) 

# returns ['Hello', ' World!']
