# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:11:50 2024

@author: khush
"""

"""
7. Creating a Bank Account Class with Inheritance
• Define a base class Account with attributes like account_no (string) and balance 
(float). Implement constructor method in Account to initialize these attributes.
• Create a subclass BankAccount that inherits from Account. 
• Add a method called deposit(amount) to BankAccount to add funds to the balance.
• Optionally, you can add a withdraw(amount) method that subtracts funds from the 
balance while considering overdraft protection (if applicable).

"""

class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

class BankAccount(Account):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful. Remaining balance:", self.balance)
        else:
            print("Insufficient funds!")


bank_acc = BankAccount("123456789", 1000.0)
print("Initial balance:", bank_acc.balance)

bank_acc.deposit(500.0)
print("After deposit:", bank_acc.balance)

bank_acc.withdraw(200.0)


"""
Initial balance: 1000.0
After deposit: 1500.0
Withdrawal successful. Remaining balance: 1300.0

"""