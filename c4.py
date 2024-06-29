# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:50:22 2024

@author: khush
"""

"""
Write a python program to create employee class that has employee details (id, name, 
salary) and design a function that reads the employee id from the user and display employee 
details along with the Net salary after adding DA(15%), MA(5%), HRA(20%) and deducting 
PA(12%) from the basic salary.

"""

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

def calculate_net_salary(salary):
    da = 0.15 * salary
    ma = 0.05 * salary
    hra = 0.20 * salary
    pa = 0.12 * salary
    net_salary = salary + da + ma + hra - pa
    return net_salary

def main():
    employees = [
        Employee(101, "khushi shah", 50000),
        Employee(102, "krisa shah", 60000),
        Employee(103, "jil shah", 75000)
    ]

    emp_id = int(input("Enter employee ID: "))
    found = False

    for emp in employees:
        if emp.emp_id == emp_id:
            found = True
            net_salary = calculate_net_salary(emp.salary)
            print("\nEmployee Details:")
            print("ID:", emp.emp_id)
            print("Name:", emp.name)
            print("Basic Salary:", emp.salary)
            print("Net Salary:", net_salary)
            break

    if not found:
        print("Employee not found!")

main()


"""
Enter employee ID: 103

Employee Details:
ID: 103
Name: jil shah
Basic Salary: 75000
Net Salary: 96000.0

"""