class Book:
    def __init__(self, title, author, price):
        self.title  = title
        self.author = author
        self.price  = price

    def __str__(self):
        return f'Book: {self.title} by {self.author} | Price: ₹{self.price}'


class Library:
    def __init__(self, name):
        self.name  = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f'Library: {self.name} | Books: {len(self.books)}'


b1 = Book('Python Basics', 'John', 499)
b2 = Book('Data Science', 'Sara', 799)
b3 = Book('Web Dev',      'Mike', 599)

lib = Library('City Library')
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print(b1)
print(b2)
print(lib)

for book in lib.books:
    print(book)