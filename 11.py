# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:37:17 2024

@author: rcc
"""

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Python is fantastic

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Python is fantastic
