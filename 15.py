# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:37:49 2024

@author: khush
"""

#loop

for x in "banana":
  print(x) 

"""
b
a
n
a
n
a

"""

a = "Hello, World!"
print(len(a))

#13

txt = "The best things in life are free!"
print("xyz" in txt)

#False

txt = "The best things in life are free!"
print("best" in txt)

#True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Yes, 'free' is present.

txt = "The best things in life are free!"
print("best" not in txt)

#False

txt = "The best things in life are free!"
print("xyz" not in txt)

#True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
 #No, 'expensive' is NOT present. 