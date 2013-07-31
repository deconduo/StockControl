'''Imports'''

from CDClass import CD
from BookClass import Book
from StockRepositoryClass import StockRepository
from StockExceptionClass import StockException

'''Classes'''

class Test(object):
    def test(self):
        # Create 5 CDs and 5 Books
        testCD1 = CD("Test CD 1", "20/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 10.00)
        testCD2 = CD("Test CD 2", "20/3/2013", "Metal", "Test Artist 2", "Test Client 2", 2, 12.35)
        testCD3 = CD("Test CD 3", "20/3/2013", "Blues", "Test Artist 3", "Test Client 3", 2, 14.52)
        testCD4 = CD("Test CD 4", "20/3/2013", "Rock", "Test Artist 4", "Test Client 4", 1, 12.00)
        testCD5 = CD("Test CD 5", "20/3/2014", "Metal", "Test Artist 5", "Test Client 5", 1, 9.40)
        testBook1 = Book("Test Book 1", "20/3/2013", "Rock", "Test Author 1", "Test Client 6", 4, 4.30)
        testBook2 = Book("Test Book 2", "20/3/2013", "Blues", "Test Author 2", "Test Client 7", 3, 9.99)
        testBook3 = Book("Test Book 3", "20/3/2013", "Metal", "Test Author 3", "Test Client 8", 4, 3.95)
        testBook4 = Book("Test Book 4", "20/3/2013", "Metal", "Test Author 4", "Test Client 9", 4, 6.78)
        testBook5 = Book("Test Book 5", "20/13/2013", "Blues", "Test Author 5", "Test Client 10", 3, 15.20)
        newStock = [testCD1, testCD2, testCD3, testCD4, testCD5, testBook1, testBook2, testBook3, testBook4, testBook5]
        
        # Add new items to Repository
        testRepository = StockRepository()
        for stockItem in newStock:
            testRepository.EnterStock(stockItem)
            
        testRepository.EnterStock(testCD1)
        
        print testCD1.IsAPreRelease()
        print testCD5.IsAPreRelease()
        
        # Calculate total holding price for all new items
        total = 0
        for stockItem in newStock:
            total += stockItem.CalculateStorageCost()
        print "Total holding price: %.2f" % (total)
        
        # Print all the stock in the Repository
        
        print testRepository
        
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