# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:03:53 2024

@author: khush
"""

#25. Write a Python function to sort a list of strings in alphabetical order.

def sort(strings):
    strings.sort()
    return strings

input_strings = input("Enter the list of strings separated by spaces: ").split()
sorted_strings = sort(input_strings)
print("Sorted list of strings:", sorted_strings)


"""
Enter the list of strings separated by spaces: khushi jil kavya dhruvi prachi
Sorted list of strings: ['dhruvi', 'jil', 'kavya', 'khushi', 'prachi']

"""

#another method

def bubble_sort(strings):
    n = len(strings)
    for i in range(n):
        for j in range(0, n-i-1):
            if strings[j] > strings[j+1]:
                strings[j], strings[j+1] = strings[j+1], strings[j]


i= input("Enter the list of strings separated by spaces: ").split()


bubble_sort(i)

print("Sorted list of strings:", i)
