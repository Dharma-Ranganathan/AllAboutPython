import time as t
# Simple Library Management project : 1
class Library: # creating class for Library
    def __init__(self,list): # Initializing the class with function
        self.books_list = list # books list creating
        self.available_books = list[:] # creating new list for available books list
        self.books_lent = {} # creating books for lent and stored as list (book as key and name as value)

    def display_books(self): # function for displaying books
        for books in self.books_list:
            print(books)

    def display_available_books(self): # function for displaying available books
        for books in self.available_books:
            print(books)

    def borrow_books(self,name,book): # function for lending books
        self.name = name
        print("Hello " + self.name)
        if book not in self.books_list:
            print("THE BOOK YOU ENTERED IS NOT IN BOOKS LIST")
            return
        if book in self.available_books:
            self.books_lent.update({book: name})
            self.available_books.remove(book)
            print("TAKE THE BOOK THAT YOU WANT IS IN AVAILABLE BOOKS LIST, ANY OTHER BOOKS YOU WANT?")
        else:
            print("THE BOOK YOU ENTERED IS TAKEN BY ANOTHER USER ALREADY, WE HAVE NO PERMISSION TO DISCLOSE THEIR NAME PUBLICLY")

    def return_books(self,book): # function for returning the lent books
        del self.books_lent[book]
        self.available_books.append(book)
        print("THE BOOK YOU RETURNED IS SUCCESSFULLY ADDED, DO YOU HAVE ANY OTHER BOOKS TO RETRUN?")


if __name__=="__main__": # storing all the objects we made in "main" module for documentation
    lib = Library(["Pharmaceutical chemistry", "Inorganic chemistry", "Organic chemistry","Physical chemistry","Analytical chemistry"])
    print("WELCOME TO LIBRARY")
    print("KINDLY ENTER YOUR OPTION FOLLOWING.....")
    t.sleep(3)
    print()
    while True: # loop for displaying the option functions we created
        print()
        print("1. Display books")
        print("2. Display Available books")
        print("3. Borrow books")
        print("4. Return books")
        print("5. Quit")
        print()
        user_choice = int(input("ENTER YOUR CHOICE: "))
        print()
        # using the if and else conditions for choosing the option we created
        if user_choice == 1:
            print("Displaying books list, Kinldy wait.....")
            t.sleep(2)
            print()
            lib.display_books()
        elif user_choice == 2:
            print("Displaying Available books list, Kinldy wait.....")
            t.sleep(2)
            print()
            lib.display_available_books()
        elif user_choice == 3:
            print("process on running.....")
            t.sleep(2)
            print()
            name = input('Enter your Name: ')
            book = input('Enter book Name: ')
            print()
            lib.borrow_books(name,book)
        elif user_choice == 4:
            print("process on running.....")
            t.sleep(2)
            print()
            book = input('Enter book Name: ')
            print()
            lib.return_books(book)
        elif user_choice == 5:
            print("you are sure to quit?.....Happy returns!!!!!")
            break
        else:
            print("you have entered Invalid number, kindly check...")





