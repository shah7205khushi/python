# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:23:54 2024

@author: khush
"""

#3) Write a python program to find type of objects in your system.

objects = [1, "hello", 3.14, [1, 2, 3], (4, 5, 6), {"a": 1, "b": 2}, True, None]


print("Type of object 1:", type(objects[0]))
print("Type of object 2:", type(objects[1]))
print("Type of object 3:", type(objects[2]))
print("Type of object 4:", type(objects[3]))
print("Type of object 5:", type(objects[4]))
print("Type of object 6:", type(objects[5]))
print("Type of object 7:", type(objects[6]))
print("Type of object 8:", type(objects[7]))

"""
output

Type of object 1: <class 'int'>
Type of object 2: <class 'str'>
Type of object 3: <class 'float'>
Type of object 4: <class 'list'>
Type of object 5: <class 'tuple'>
Type of object 6: <class 'dict'>
Type of object 7: <class 'bool'>
Type of object 8: <class 'NoneType'>

"""