# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:34:38 2024

@author: khush
"""

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self, current_date):
        dob_year, dob_month, dob_day = self.dob.split('-')
        current_year, current_month, current_day = current_date.split('-')

        age = int(current_year) - int(dob_year) - ((int(current_month), int(current_day)) < (int(dob_month), int(dob_day)))
        return age

# Example usage:
name = input("Enter person's name: ")
country = input("Enter person's country: ")
dob = input("Enter person's date of birth (YYYY-MM-DD): ")

current_date = input("Enter the current date (YYYY-MM-DD): ")

person = Person(name, country, dob)
age = person.calculate_age(current_date)
print(f"{person.name} is {age} years old.")

"""
Enter person's name: khushi
Enter person's country: ahmedabad
Enter person's date of birth (YYYY-MM-DD): 2005-02-07
Enter the current date (YYYY-MM-DD): 2024-06-12
khushi is 19 years old.

"""