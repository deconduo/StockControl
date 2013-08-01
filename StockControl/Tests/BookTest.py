import unittest
from ..Classes.BookClass import Book

class BookTest(unittest.TestCase):
    def setUp(self):
        self.testBook1 = Book("Test Book 1", "11/3/2013", "Rock", "Test Author 1", "Test Client 6", 2, 21.00)
        self.testBook2 = Book("Test Book 2", "12/3/2013", "Blues", "Test Author 2", "Test Client 7", 3, 22.00)

    def tearDown(self):
        pass
