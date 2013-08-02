'''Imports'''

from ..Classes.CDClass import CD
from ..Classes.BookClass import Book
from ..Classes.StockRepositoryClass import StockRepository
from ..Classes.StockExceptionClass import StockException

'''Classes'''

class Test(object):
    def test(self):
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