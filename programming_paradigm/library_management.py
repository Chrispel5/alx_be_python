class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        # append into the private list, not a non-existent self.books
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                return
        print(f"Book '{title}' is not available")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                return
        # only print if we never found one to return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
