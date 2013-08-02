'''Imports'''

from ..Classes.CDClass import CD
from ..Classes.BookClass import Book
from ..Classes.StockRepositoryClass import StockRepository
from ..Classes.StockExceptionClass import StockException

'''Classes'''

class TestClass(object):
    def test(self):
        # Set up a new Repository
        testRepository = StockRepository()
        
        # Create 5 CDs and 5 Books
        testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        testCD2 = CD("Test CD 2", "2/3/2013", "Metal", "Test Artist 2", "Test Client 2", 2, 12.00)
        testCD3 = CD("Test CD 3", "3/3/2013", "Blues", "Test Artist 3", "Test Client 3", 3, 13.00)
        testCD4 = CD("Test CD 4", "4/3/2013", "Rock", "Test Artist 4", "Test Client 4", 4, 14.00)
        testCD5 = CD("Test CD 5", "5/3/2014", "Metal", "Test Artist 5", "Test Client 5", 1, 15.00)
        testBook1 = Book("Test Book 1", "11/3/2013", "Rock", "Test Author 1", "Test Client 6", 2, 21.00)
        testBook2 = Book("Test Book 2", "12/3/2013", "Blues", "Test Author 2", "Test Client 7", 3, 22.00)
        testBook3 = Book("Test Book 3", "13/3/2013", "Metal", "Test Author 3", "Test Client 8", 4, 23.00)
        testBook4 = Book("Test Book 4", "14/3/2013", "Metal", "Test Author 4", "Test Client 9", 1, 24.00)
        testBook5 = Book("Test Book 5", "15/3/2013", "Blues", "Test Author 5", "Test Client 10", 2, 25.00)
        
        # Add items to an array
        newStock = [testCD1, testCD2, testCD3, testCD4, testCD5, testBook1, testBook2, testBook3, testBook4, testBook5]
        
        # Calculate total holding price for all new items
        total = 0
        for stockItem in newStock:
            total += stockItem.CalculateStorageCost()
        print "Total holding price: %.2f" % (total)
        
        # Enter items into the repository
        for stockItem in newStock:
            testRepository.EnterStock(stockItem)
        
        # Print all the stock in the repository
        print "Repository contains:\n",testRepository
        
        # Add all stock in warehouse 4
        value = testRepository.AddAllStockInWarehouse(4)
        print 'Warehouse 4 total value is: ',value
        
        # Move items to warehouse 3
        for stockItem in newStock:
            testRepository.MoveStock(stockItem.uniqueID, 3)

        # Add all stock in warehouse 4 (should now be empty)
        value = testRepository.AddAllStockInWarehouse(4)
        print 'Warehouse 4 total value is: ',value
        
        # Delete all stock
        for stockItem in newStock:
            testRepository.DeleteStock(stockItem.uniqueID)
            
        # Print all the stock in the repository (should now be empty)
        print "Repository contains:\n",testRepository