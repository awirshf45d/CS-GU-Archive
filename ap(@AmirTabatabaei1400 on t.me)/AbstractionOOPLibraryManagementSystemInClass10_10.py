from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, ISBN, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.quantity = quantity
    def __str__(self):
        return "Title: %s, Author(s): %s, ISBN:%s, Quantity: %f"%(self.title,self.author,self.ISBN,self.quantity) 
    def check_out(self):
        if self.quantity > 0:
            self.quantity -= 1
            return True
        else:
            print(self.title, " Book is NOT available for checking out")
            return False
    def return_book(self):
        self.quantity += 1


class Customer:
    def __init__(self, name, customer_id, books_checked_out, books_returned ):
        self.name = name
        self.customer_id = customer_id
        self.books_checked_out = books_checked_out
        self.books_returned = books_returned
    def __str__(self):
        return "The first name last name: %s, ID:%s"%(self.name,self.customer_id)
    def check_out_book(self, book):
        if book.check_out() and (book not in self.books_checked_out):
            self.books_checked_out.append(book)
            print(self.name ," checked out", book.title)
        else:
            print(self.name, " is not able to check out", book.title)

    def return_book(self, book):
        if book.title in self.books_checked_out:
            book.return_book()
            self.books_checked_out.remove(book)
            self.books_returned.append(book.title)
            print(self.name, " returned",  book.title)
        else:
            print(self.name, " has not checked out ", book.title)
class Transaction(ABC):
    def __init__(self, book, customer):
        self.book = book
        self.customer = customer
    
    @abstractmethod
    def Implement_transaction(self):
        pass

    def __str__(self):
        return "Transaction details: Book:%s,Customer:%s with ID:%s"%(self.book.title,self.customer.name, self.customer.customer_id) 
        print("Transacted book:",self.book.title)
        print("Customer: ", self.customer.name, "with ID: ", self.customer.customer_id)



class CheckOutTransaction(Transaction):
    def Implement_transaction(self):
        if self.book.check_out() and (self.book not in self.customer.books_checked_out):
            self.customer.books_checked_out.append(self.book)
            print("The check out transaction has been recorded for book: ", self.book.title," and customer: ", self.customer.name) 
class ReturnTransaction(Transaction):
    def Implement_transaction(self):
        if self.book in self.customer.books_checked_out:
            self.book.return_book()
            self.customer.books_checked_out.remove(self.book.title)
            print("The return transaction has been recorded for book: ", self.book.title , " and customer: ", self.customer.name)
        else:
            print("The book was not checked out so far!")



class Library:
    def __init__(self):
        self.books = []
        self.customers = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def add_customer(self, customer):
        self.customers.append(customer)
    def del_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        return False
    def del_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)
            return True
        return False
    def Implement_transaction(self,transaction_type, book, customer):
        if book in self.books and customer in self.customers:
            if transaction_type == "C":
                transaction = CheckOutTransaction(book, customer)
            elif transaction_type == "R":
                transaction = ReturnTransaction(book, customer)
            else:
                print("Invalid transaction!!!! Please select 'R' for return or 'C' for check out.")
                return
            transaction.Implement_transaction()
            self.transactions.append(transaction)
        else:
            print("Invalid book or customer.")
    def GenerateReport(self):
        print("list of the customers:" )

        for i in self.Customers:
            print(i)
        print("List of books:")

        for j in self.Books:
            print(j)
    def SearchBook(self , ISBNOfBook):
        for i in self.Books:
            if ISBNOfBook == i.ISBN:
                print("the result(s) of your search is:")
                print(i)
    def SearchCustomer(self  , IDOfCustomer):
        for i in self.Customers:
            if i.customer_id == IDOfCustomer:
                print(i)
    def SearchTransaction(self , bookISBN , customerID):
        res = []
        for i in self.transactions:
            if i.book.ISBN == bookISBN and i.customer.customer_id == customerID:
                print(i)
                 
            
#defining the required objects:
book1 = Book("CalculusI", "Silverman", "123456789", 10) 
book2 = Book("Engineering Calculus", "Thomas", "213457908", 8)

customer1 = Customer("Ahmad Rezaei" , "9089236576", [])
customer2 = Customer("Maryam Ahmadi" , "3457865290", [])

#adding the books to the library 
library =  Library()
library.add_book(book1)
library.add_book(book2)

#adding the customers
library.add_customer(customer1)
library.add_customer(customer2)

#implementing transaction
library.Implement_transaction("C", book1, customer1)
library.Implement_transaction("C", book1, customer2)
library.Implement_transaction("C", book2, customer1)
library.Implement_transaction("C", book2, customer2)

library.Implement_transaction("R", book1, customer1)
library.Implement_transaction("C", book2, customer2)

library.Implement_transaction("R", book1, customer1)
library.Implement_transaction("C", book2, customer2)

library.Implement_transaction("R", book1, customer1)
library.Implement_transaction("C", book2, customer2)

library.Implement_transaction("R", book1, customer1)
#desplaying books, customers, transactions
for book in library.books:
    print("#########################")
    book.display_details()

for customer in library.customers:
    print("#########################")
    customer.display_customer_info()
print("############LIST OF ALL TRANSACTIONS:#####################")
for transaction in library.transactions:
    print("##")
    transaction.display_transaction_info()



