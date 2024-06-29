# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:56:45 2024

@author: khush
"""

class Book:
    def __init__(self, ISBN, book_name, no_of_pages, author):
        self.ISBN = ISBN
        self.book_name = book_name
        self.no_of_pages = no_of_pages
        self.author = author

class Purchased(Book):
    def __init__(self, ISBN, book_name, no_of_pages, author, price):
        self.price = price
        super().__init__(ISBN, book_name, no_of_pages, author)

class Donated(Book):
    def __init__(self, ISBN, book_name, no_of_pages, author, is_new):
        self.is_new = is_new
        super().__init__(ISBN, book_name, no_of_pages, author)

class Collection(Purchased, Donated):
    def __init__(self, ISBN, book_name, no_of_pages, author, price, is_new, subject, qty):
        self.subject = subject
        self.qty = qty
        if price:
            Purchased.__init__(self, ISBN, book_name, no_of_pages, author, price)
        else:
            Donated.__init__(self, ISBN, book_name, no_of_pages, author, is_new)

    def display_details(self):
        print("Book Details:")
        print(f"ISBN: {self.ISBN}")
        print(f"Book Name: {self.book_name}")
        print(f"Number of Pages: {self.no_of_pages}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}" if isinstance(self, Purchased) else "Donated")
        print(f"Condition: {'New' if self.is_new else 'Used'}" if isinstance(self, Donated) else "Purchased")
        print(f"Subject: {self.subject}")
        print(f"Quantity: {self.qty}")


# Read data for books from the user
def read_books():
    books = []

    n = int(input("Enter the number of books: "))
    for _ in range(n):
        ISBN = input("Enter ISBN: ")
        book_name = input("Enter book name: ")
        no_of_pages = int(input("Enter number of pages: "))
        author = input("Enter author: ")
        price = float(input("Enter price (if purchased, else enter 0): "))
        is_new = input("Is it new? (yes/no): ").lower() == 'yes'
        subject = input("Enter subject: ")
        qty = int(input("Enter quantity: "))

        if price:
            books.append(Purchased(ISBN, book_name, no_of_pages, author, price))
        else:
            books.append(Donated(ISBN, book_name, no_of_pages, author, is_new))

    return books


# Display details of books
def display_books(books):
    for book in books:
        book.display_details()
        print()


# Main function
def main():
    books = read_books()
    display_books(books)


main()
