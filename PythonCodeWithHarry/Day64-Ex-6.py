# Exercise Solution 6.

print("---Library Management System---")

class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def addBooks(self):
     while True:
      bookname = input("Add a Book: ")
      if bookname.lower() == 'done':
         break
      else:
       self.books.append(bookname)
       self.no_of_books += 1
       print(f"{bookname} Added Successfully.")


    def showBooks(self):
       if self.no_of_books == 0:
          print("Library is Empty!") 
       else:
          print("Books in the Library")
          for i, book in enumerate(self.books, 1): 
             print(f"{i}. {book}") 

    def countBooks(self):
       return self.no_of_books


lib = Library()
lib.addBooks()
lib.showBooks()
print("Total Books In the Library", lib.countBooks())
