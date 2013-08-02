'''Imports'''
import unittest
from ..Classes.BookClass import Book
from ..Classes.StockExceptionClass import StockException

'''Classes'''
class BookTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Tests the __str__ function
    def testStr(self):
        self.testBook1 = Book("Test Book 1", "11/3/2013", "Rock", "Test Author 1", "Test Client 6", 2, 21.00)
        self.assertEqual(self.testBook1.__str__(), "----------\n" + super(Book, self.testBook1).__str__() + "\n Title: %s, Release Date: %s, Genre: %s, Author: %s" % (self.testBook1.title, self.testBook1.GetDateReleased(), self.testBook1.genre, self.testBook1.author))
        
    # Tests that the title must be a string. Gives an array instead, and tests for an exception.
    def testInitTitleException1(self):
        self.assertRaises(StockException, Book, [], "11/3/2013", "Rock", "Test Author 1", "Test Client 6", 2, 21.00)
        
    # Tests that the title must be less than 100 characters. Gives a long title instead, and tests for an exception.
    def testInitTitleException2(self):
        self.assertRaises(StockException, Book, "Extra long title -------------------------------------------------------------------------------------", "11/3/2013", "Rock", "Test Author 1", "Test Client 6", 2, 21.00)
        
    # Tests that the date is in a valid format. Gives a bad date instead, and tests for an exception.
    def testInitDateException(self):
        self.assertRaises(StockException, Book, "Test Book 1", "50/3/2013", "Rock", "Test Author 1", "Test Client 6", 2, 21.00)
        
    # Tests that the genre must be a string. Gives an array instead, and tests for an exception.
    def testInitGenreException1(self):
        self.assertRaises(StockException, Book, "Test Book 1", "11/3/2013", [], "Test Author 1", "Test Client 6", 2, 21.00)
        
    # Tests that the genre must be either Rock, Metal or Blues. Gives Jazz instead, and tests for an exception.
    def testInitGenreException2(self):
        self.assertRaises(StockException, Book, "Test Book 1", "11/3/2013", "Jazz", "Test Author 1", "Test Client 6", 2, 21.00)
        
    # Tests that the author must be a string. Gives an array instead, and tests for an exception.
    def testInitAuthorException(self):
        self.assertRaises(StockException, Book, "Test Book 1", "11/3/2013", "Rock", [], "Test Client 6", 1, 11.00)
    
    # Tests the GetDateReleased method   
    def testDateReleased(self):
        self.testBook1 = Book("Test Book 1", "11/3/2013", "Rock", "Test Author 1", "Test Client 6", 2, 21.00)
        self.assertEqual(self.testBook1.GetDateReleased(), "11/March/2013")

    # Tests the isAPreRelease method
    def testPreRelease(self):
        self.testBook1 = Book("Test Book 1", "11/3/2013", "Rock", "Test Author 1", "Test Client 6", 2, 21.00)
        self.testBook2 = Book("Test Book 2", "12/3/2014", "Blues", "Test Author 2", "Test Client 7", 3, 22.00)
        self.assertEqual(self.testBook1.IsAPreRelease(), False)
        self.assertEqual(self.testBook2.IsAPreRelease(), True)
        
    # Tests multiply method is working.
    def testCalculateStorageCost(self):
        self.testBook1 = Book("Test Book 1", "11/3/2013", "Rock", "Test Author 1", "Test Client 6", 2, 21.00)
        self.testStorage = self.testBook1.CalculateStorageCost()
        self.assertEqual(self.testStorage, 2.05)
