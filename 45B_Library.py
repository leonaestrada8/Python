

class LibrarySystem:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = author

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]

    def find_book_by_title(self, title):
        return self.books.get(title, None)

    def list_books(self):
        return self.books


import unittest

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.library = LibrarySystem()
        self.library.add_book("The Hobbit", "J.R.R. Tolkien")
        self.library.add_book("Dune", "Frank Herbert")

    def test_add_book(self):
        self.library.add_book("Foundation", "Isaac Asimov")
        self.assertEqual(self.library.find_book_by_title("Foundation"), "Isaac Asimov")

    def test_remove_book(self):
        self.library.remove_book("The Hobbit")
        self.assertIsNone(self.library.find_book_by_title("The Hobbit"))

    def test_find_book_by_title(self):
        self.assertEqual(self.library.find_book_by_title("Dune"), "Frank Herbert")

    def test_list_books(self):
        books = {
            "The Hobbit": "J.R.R. Tolkien",
            "Dune": "Frank Herbert"
        }
        self.assertEqual(self.library.list_books(), books)

if __name__ == '__main__':
    unittest.main()
