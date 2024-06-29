# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:44:49 2024

@author: khush
"""

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def square(self):
        return self.number1 ** 2, self.number2 ** 2

    def cube(self):
        return self.number1 ** 3, self.number2 ** 3

    def difference(self):
        return abs(self.number1 - self.number2)


# Menu-driven program
def main():
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    calc = Calculator(number1, number2)

    print("\nMenu:")
    print("1. Calculate square")
    print("2. Calculate cube")
    print("3. Calculate difference")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        result1, result2 = calc.square()
        print(f"Square of {number1} is {result1}")
        print(f"Square of {number2} is {result2}")
    elif choice == 2:
        result1, result2 = calc.cube()
        print(f"Cube of {number1} is {result1}")
        print(f"Cube of {number2} is {result2}")
    elif choice == 3:
        result = calc.difference()
        print(f"Difference between {number1} and {number2} is {result}")
    else:
        print("Invalid choice")


main()

"""
Enter first number: 5
Enter second number: 10

Menu:
1. Calculate square
2. Calculate cube
3. Calculate difference
Enter your choice (1/2/3): 1
Square of 5.0 is 25.0
Square of 10.0 is 100.0

runfile('D:/sem 4/python/e2.py', wdir='D:/sem 4/python')
Enter first number: 2
Enter second number: 67

Menu:
1. Calculate square
2. Calculate cube
3. Calculate difference
Enter your choice (1/2/3): 2
Cube of 2.0 is 8.0
Cube of 67.0 is 300763.0

runfile('D:/sem 4/python/e2.py', wdir='D:/sem 4/python')
Enter first number: 66
Enter second number: 3

Menu:
1. Calculate square
2. Calculate cube
3. Calculate difference
Enter your choice (1/2/3): 3
Difference between 66.0 and 3.0 is 63.0

"""