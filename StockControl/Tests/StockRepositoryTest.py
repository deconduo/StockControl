import unittest
from ..Classes.StockRepositoryClass import StockRepository
from ..Classes.CDClass import CD
from ..Classes.BookClass import Book

class StockRepositoryTest(unittest.TestCase):
    def setUp(self):
        # Create 5 CDs and 5 Books
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testCD2 = CD("Test CD 2", "2/3/2013", "Metal", "Test Artist 2", "Test Client 2", 2, 12.00)
        self.testCD3 = CD("Test CD 3", "3/3/2013", "Blues", "Test Artist 3", "Test Client 3", 3, 13.00)
        self.testCD4 = CD("Test CD 4", "4/3/2013", "Rock", "Test Artist 4", "Test Client 4", 4, 14.00)
        self.testCD5 = CD("Test CD 5", "5/3/2014", "Metal", "Test Artist 5", "Test Client 5", 1, 15.00)
        self.testBook1 = Book("Test Book 1", "11/3/2013", "Rock", "Test Author 1", "Test Client 6", 2, 21.00)
        self.testBook2 = Book("Test Book 2", "12/3/2013", "Blues", "Test Author 2", "Test Client 7", 3, 22.00)
        self.testBook3 = Book("Test Book 3", "13/3/2013", "Metal", "Test Author 3", "Test Client 8", 4, 23.00)
        self.testBook4 = Book("Test Book 4", "14/3/2013", "Metal", "Test Author 4", "Test Client 9", 1, 24.00)
        self.testBook5 = Book("Test Book 5", "15/3/2013", "Blues", "Test Author 5", "Test Client 10", 2, 25.00)
        # Add items to an array
        self.newStock = [self.testCD1, self.testCD2, self.testCD3, self.testCD4, self.testCD5, self.testBook1, self.testBook2, self.testBook3, self.testBook4, self.testBook5]
        # Set up a new Repository
        self.testRepository = StockRepository()

    def tearDown(self):
        pass
    
    def testEnterStock(self):
        # Add new items to Repository
        for stockItem in self.newStock:
            self.testRepository.EnterStock(stockItem)
        # Check that there are 10 items in the repository
        self.assertEqual(len(self.testRepository.stockCollection), 10)
