# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:41:08 2024

@author: khush
"""

class BankAc:
    def __init__(self, ac_no, acc_holder_name, contact, age):
        self.ac_no = ac_no
        self.acc_holder_name = acc_holder_name
        self.contact = contact
        self.age = age
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully. Current balance: {self.balance}")

    def display_details(self):
        print(f"Account Number: {self.ac_no}")
        print(f"Account Holder Name: {self.acc_holder_name}")
        print(f"Contact: {self.contact}")
        print(f"Age: {self.age}")
        print(f"Current Balance: {self.balance}")

class Customer(BankAc):
    def __init__(self, ac_no, acc_holder_name, contact, age):
        super().__init__(ac_no, acc_holder_name, contact, age)

    def current_balance(self):
        return self.balance

def main():
    ac_no = input("Enter account number: ")
    acc_holder_name = input("Enter account holder name: ")
    contact = input("Enter contact number: ")
    age = int(input("Enter age: "))

    customer = Customer(ac_no, acc_holder_name, contact, age)

    while True:
        print("\nMenu")
        print("1. Display Account Details")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Check Current Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer.display_details()

        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            customer.deposit(amount)

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            customer.withdraw(amount)

        elif choice == '4':
            print(f"Current Balance: {customer.current_balance()}")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()
