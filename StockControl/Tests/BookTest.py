import unittest
from ..Classes.BookClass import Book

class BookTest(unittest.TestCase):
    def setUp(self):
        self.testBook1 = Book("Test Book 1", "20/3/2013", "Rock", "Test Author 1", "Test Client 6", 4, 4.30)
        self.testBook2 = Book("Test Book 2", "20/3/2013", "Blues", "Test Author 2", "Test Client 7", 3, 9.99)

    def tearDown(self):
        pass
