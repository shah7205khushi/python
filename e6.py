# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:23:36 2024

@author: khush
"""

class Employee:
    def __init__(self, emp_id, emp_nm, designation, department):
        self.emp_id = emp_id
        self.emp_nm = emp_nm
        self.designation = designation
        self.department = department

class Company:
    def __init__(self, company_nm):
        self.company_nm = company_nm

class Comp_Employee(Employee, Company):
    def __init__(self, emp_id, emp_nm, designation, department, company_nm, salary, experience_yrs):
        Employee.__init__(self, emp_id, emp_nm, designation, department)
        Company.__init__(self, company_nm)
        self.salary = salary
        self.experience_yrs = experience_yrs

    def display_details(self):
        print("Company Employee Details:")
        print(f"Company Name: {self.company_nm}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_nm}")
        print(f"Designation: {self.designation}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print(f"Experience: {self.experience_yrs} years")

# Main function to read data from the user and display employee details
def main():
    company_nm = input("Enter company name: ")
    
    employees = []
    while True:
        emp_id = input("Enter employee ID: ")
        emp_nm = input("Enter employee name: ")
        designation = input("Enter designation: ")
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))
        experience_yrs = int(input("Enter years of experience: "))
        
        comp_employee = Comp_Employee(emp_id, emp_nm, designation, department, company_nm, salary, experience_yrs)
        employees.append(comp_employee)
        
        cont = input("Do you want to add another employee? (yes/no): ")
        if cont.lower() != 'yes':
            break
    
    dept_to_display = input("Enter the department to display: ")
    
    print(f"\nEmployees in department {dept_to_display}:")
    for emp in employees:
        if emp.department == dept_to_display:
            emp.display_details()

if __name__ == "__main__":
    main()


"""

Enter company name: s
Enter employee ID: 3
Enter employee name: d
Enter designation: f
Enter department: d
Enter salary: 33333
Enter years of experience: 2
Do you want to add another employee? (yes/no): yes
Enter employee ID: 1
Enter employee name: s
Enter designation: s
Enter department: s
Enter salary: 33
Enter years of experience: 2
Do you want to add another employee? (yes/no): no
Enter the department to display: s

Employees in department s:
Company Employee Details:
Company Name: s
Employee ID: 1
Employee Name: s
Designation: s
Department: s
Salary: 33.0
Experience: 2 years

"""