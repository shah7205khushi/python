# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:34:25 2024

@author: rcc
"""

# global variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Python is awesome


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Python is fantastic
#Python is awesome