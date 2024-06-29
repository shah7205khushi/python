# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:01:58 2024

@author: khush
"""

#Write a Python function to create a dictionary with keys as numbers from 1 to N and values
#as squares of the keys.

def create_square_dict(N):
    return {i: i * i for i in range(1, N + 1)}

# Example usage:
N = 5
square_dict = create_square_dict(N)
print(square_dict)  

#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
