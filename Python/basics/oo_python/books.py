class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


class BookCase:
    def __init__(self, books=None):
        self.books = books

    @classmethod
    def create_bookcase(cls, book_list): # cls means class method takes a class and returns a class
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)
