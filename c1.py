# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:49:17 2024

@author: khush
"""

"""
1. Define a Book class with attributes like title, author, and no_of_pages (all strings). 
Implement constructor(s) to initialize these attributes when creating a new Book object. Add 
a method called describe_book() that prints a summary of the book's information.

"""

class Book:
    def __init__(self, title, author, no_of_pages):
        self.title = title
        self.author = author
        self.no_of_pages = no_of_pages

    def describe_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Number of Pages:", self.no_of_pages)


book1 = Book("khushi", "J.K. shah", "300")
book1.describe_book()

"""
Title: khushi
Author: J.K. shah
Number of Pages: 300

"""