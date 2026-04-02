class Book:

    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if not self.available:
            print("Already borrowed!")
            return
        self.available = False
        print(f"Borrowed: {self.title}")

    def return_book(self):
        if self.available:
            print("Book is already available!")
            return
        self.available = True
        print(f"Returned: {self.title}")


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def available_books(self):
        available = [book.title for book in self.books if book.available]
        print(", ".join(available))

    def search(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Found: {book.title} by {book.author}")
                return
        print("Book not found!")


# Demo
b1 = Book('Python Basics', 'John', True)
b2 = Book('Data Science', 'Sara', True)
b3 = Book('Web Dev', 'Mike', True)

lib = Library('City Library')
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

b1.borrow()               
b1.borrow()               
lib.available_books()     
b1.return_book()          
lib.available_books()     
lib.search('data science')