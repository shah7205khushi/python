# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:53:53 2024

@author: khush
"""

"""
Define class student with attributes like First_name, Last_name, Course, batch_year, result). 
Apply constructor (s) to initialize the attributes while creating new student object. Here, 
batch_year must be passing year and result must be PASS or FAIL. Add a method to calculate 
total number of FAIL students. (static method).
"""

class Student:
    fail_count = 0

    def __init__(self, first_name, last_name, course, batch_year, result):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.batch_year = batch_year
        self.result = result
        if result == "FAIL":
            Student.fail_count += 1


    def total_fail_students():
        return Student.fail_count


student1 = Student("khushi", "shah", "Engineering", 2023, "PASS")
student2 = Student("jil", "shah", "M.B.A", 2022, "FAIL")
student3 = Student("Bina", "Joshi", "Computer Science", 2023, "FAIL")

print("Total number of FAIL students:", Student.total_fail_students())

"""
Total number of FAIL students: 2

"""
