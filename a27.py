# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 23:30:46 2024

@author: khush
"""

#27) Write a python program to make a simple calculator to add, subtract, multiply or divide

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print(num1, "/", num2, "=", num1 / num2)
else:
     print("Invalid Input")
     
     
"""

output

Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice (1/2/3/4): 3
Enter first number: 5
Enter second number: 7
5 * 7 = 35

"""     
