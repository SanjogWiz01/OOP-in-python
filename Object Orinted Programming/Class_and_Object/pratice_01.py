''' Library System:
Class Book and Library.
Library can add_book(), lend_book(), return_book().

Employee Payroll:'''
# core concept
''' 📚 1. Library System
🎯 Goal:

To manage books in a library using Object-Oriented Programming — we’ll create objects to represent both Books and the Library that stores and manages them.

🧩 Classes Involved:
🔹 Class: Book

Represents a single book in the library.

Each Book object will have:

title (e.g., “Python Crash Course”)

author

available (True/False to show if it’s currently borrowed)

✅ The Book class is like a blueprint for each book — it just holds information about one item.

🔹 Class: Library

Represents the entire library.

The library will have:

A list (or collection) of Book objects.

Methods (functions) to manage them.

Main Methods:

add_book()

Adds a new book object to the library’s list.

Like storing a new book in the library shelf.

lend_book()

Marks a book as borrowed (not available).

The system checks if the book exists and isn’t already lent.

return_book()

Marks a previously lent book as available again.

It’s like putting the book back on the shelf.

💡 Concept Focus:

Encapsulation: Data (title, author, available) and methods (lend, return) are combined in one object.

Objects interaction: Library object uses Book objects to perform tasks.

Real-world mapping: Just like a real library manages books and their borrowing system.'''
class book:
     def __init__(self,faculity,title,available=True):
          self.faculity=faculity
          self.title=title
          self.available=available
class library:
    def __init__(self):
         self.books=[]
    def add_book(self,book):
         self.books.append(book)
         print(f'Book "{book.title}" added to the library.')
    def lend_book(self,title):

            for book in self.books:
                if book.title==title:
                    if book.available:
                            book.available=False
                            print(f'You have borrowed "{book.title}".')
                            return
                    else:
                            print(f'Sorry, "{book.title}" is currently not available.')
                            return
            print(f'Sorry, the book "{title}" is not in the library.')
    def return_book(self,title):
            for book in self.books:
                if book.title==title:
                    book.available=True
                    print(f'You have returned "{book.title}".')
                    return
            print(f'Sorry, the book "{title}" does not belong to this library.')
# --------- Test the Library System ------------
lib = library()
book1 = book("Science","Physics 101")
book2 = book("Math","Calculus Basics")
lib.add_book(book1)
lib.add_book(book2)
lib.lend_book("Physics 101")
lib.lend_book("Physics 101")  # trying to lend again
lib.return_book("Physics 101")
lib.lend_book("Calculus Basics")
lib.return_book("Calculus Basics")
lib.return_book("Biology Basics")  # trying to return a book not in library
