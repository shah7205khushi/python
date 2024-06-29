# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:44:16 2024

@author: khush
"""

class Apparel:
    def __init__(self, apr_name, gender, size, price):
        self.apr_name = apr_name
        self.gender = gender
        self.size = size
        self.price = price

    def read_data(self):
        self.apr_name = input("Enter apparel name: ")
        self.gender = input("Enter gender (M/F): ")
        self.size = input("Enter size: ")
        self.price = float(input("Enter price: "))

    def display_data(self):
        print(f"Apparel Name: {self.apr_name}")
        print(f"Gender: {self.gender}")
        print(f"Size: {self.size}")
        print(f"Price: {self.price}")

class WesternClothing(Apparel):
    def __init__(self, apr_name, gender, size, price, is_imported, qty):
        super().__init__(apr_name, gender, size, price)
        self.is_imported = is_imported
        self.qty = qty

    def read_data(self):
        super().read_data()
        self.is_imported = input("Is the apparel imported? (yes/no): ").lower() == 'yes'
        self.qty = int(input("Enter quantity: "))

    def display_data(self):
        super().display_data()
        print(f"Imported: {self.is_imported}")
        print(f"Quantity: {self.qty}")

class TraditionalClothing(Apparel):
    def __init__(self, apr_name, gender, size, price, is_designer, qty):
        super().__init__(apr_name, gender, size, price)
        self.is_designer = is_designer
        self.qty = qty

    def read_data(self):
        super().read_data()
        self.is_designer = input("Is the apparel designer? (yes/no): ").lower() == 'yes'
        self.qty = int(input("Enter quantity: "))

    def display_data(self):
        super().display_data()
        print(f"Designer: {self.is_designer}")
        print(f"Quantity: {self.qty}")

class Bill(WesternClothing, TraditionalClothing):
    def __init__(self, bill_no, name, contact, total_amount, apr_name, gender, size, price, is_imported, is_designer, qty):
        WesternClothing.__init__(self, apr_name, gender, size, price, is_imported, qty)
        TraditionalClothing.__init__(self, apr_name, gender, size, price, is_designer, qty)
        self.bill_no = bill_no
        self.name = name
        self.contact = contact
        self.total_amount = total_amount

    def read_data(self):
        self.bill_no = input("Enter bill number: ")
        self.name = input("Enter customer name: ")
        self.contact = input("Enter contact number: ")
        self.total_amount = float(input("Enter total amount: "))

    def display_data(self):
        print(f"Bill Number: {self.bill_no}")
        print(f"Customer Name: {self.name}")
        print(f"Contact Number: {self.contact}")
        print(f"Total Amount: {self.total_amount}")
        print("Purchased Apparel Details:")
        super().display_data()

def main():
    # Create objects and read data
    apr_name = input("Enter apparel name: ")
    gender = input("Enter gender (M/F): ")
    size = input("Enter size: ")
    price = float(input("Enter price: "))
    is_imported = input("Is the apparel imported? (yes/no): ").lower() == 'yes'
    is_designer = input("Is the apparel designer? (yes/no): ").lower() == 'yes'
    qty = int(input("Enter quantity: "))
    bill_no = input("Enter bill number: ")
    name = input("Enter customer name: ")
    contact = input("Enter contact number: ")
    total_amount = float(input("Enter total amount: "))

    # Create Bill object
    bill = Bill(bill_no, name, contact, total_amount, apr_name, gender, size, price, is_imported, is_designer, qty)

    # Display data
    bill.display_data()

if __name__ == "__main__":
    main()
