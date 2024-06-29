# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:58:04 2024

@author: khush
"""

#6. Write a Python function to convert a CamelCase string to snake_case.


def camel_to_snake(camel):
    snake = ''
    for char in camel:
        if char.isupper():
            snake += '_' + char.lower()
        else:
            snake += char
    return snake.lstrip('_')

# Example usage:
camel_input = input("Enter a CamelCase string: ")
snake_output = camel_to_snake(camel_input)
print("Snake case output:", snake_output)

"""
Enter a CamelCase string: KHUSHI
Snake case output: k_h_u_s_h_i

"""