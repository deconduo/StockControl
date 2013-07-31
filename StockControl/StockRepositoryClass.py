'''Imports'''
from StockExceptionClass import StockException

'''Classes'''
class StockRepository(object):
    
    # Creates an empty array for the storage of StockItems when object is created.
    def __init__(self):
        print 'Creating a StockRepository'
        self.stockCollection = []
    
    # Prints each StockItem in a readable format.    
    def __str__(self):
        print 'Printing StockRepository information'
        repositoryDesc = ""
        for stockItem in self.stockCollection:
             repositoryDesc += (str(stockItem) + "\n")
        return repositoryDesc
    
    # Adds a StockItem to the Repository, checks to make sure it doesn't exist in there beforehand.
    def EnterStock(self, stockItem):
        print 'Adding a StockItem to a Repository'
        try:
            if stockItem not in self.stockCollection:
                    self.stockCollection.append(stockItem)
            else:
                raise StockException('StockRepository', 'EnterStock', 'The item you attempted to add already exists in repository.')
        except StockException as error:
            print error
        
    # Moves a list of stockItems to a new warehouse. Checks that the uniqueIDs and the warehouseNumber are viable.
    def MoveStock(self, uniqueIDs, warehouseNumberInt):
        print 'Moving stock to a new warehouse'
        try:
            if isinstance(warehouseNumberInt, int):
                if 0 < warehouseNumberInt < 5:
                    for stockItem in self.stockCollection:
                        if isinstance(uniqueIDs, int) == True:
                            if stockItem.uniqueID == uniqueIDs:
                                stockItem.warehouseNumber = warehouseNumberInt
                        elif isinstance(uniqueIDs, array) == True:                
                            if stockItem.uniqueID in uniqueIDs:
                                stockItem.warehouseNumber = warehouseNumberInt
                        else:
                            raise StockException('StockRepository', 'MoveStock', 'You must provide either a single uniqueID or an array of uniqueIDs')
                else:
                    raise StockException('StockRepository', 'MoveStock', 'Warehouse number must be between 1 and 4.')
            else:
               raise StockException('StockRepository', 'MoveStock', 'Warehouse number must be an integer.')
        except StockException as error:
            print error
    
    # Deletes stock from the repository. Checks to make sure the uniqueIDs given are viable.
    def DeleteStock(self, uniqueIDs):
        print 'Deleting stock from repository'
        try:
            for stockItem in self.stockCollection:
                if isinstance(uniqueIDs, int) == True:
                    if stockItem.uniqueID == uniqueIDs:
                        self.stockCollection.remove(stockItem)
                elif isinstance(uniqueIDs, array) == True:
                    if stockItem.uniqueID in uniqueIDs:
                        self.stockCollection.remove(stockItem)
                else:
                    raise StockException('StockRepository', 'DeleteStock', 'You must provide either a single uniqueID or an array of uniqueIDs')
        except StockException as error:
            print error
    
    # Adds up all the stock in a warehouse. Checks that the warehouse number given is viable.
    def AddAllStockInWarehouse(self, warehouseNumberInt):
        print 'Adding all stock in a warehouse'
        try:
            if isinstance(warehouseNumberInt, int):
                if 0 < warehouseNumberInt < 5: 
                    total = 0
                    for item in self.stockCollection:
                        if item.warehouseNumber == warehouseNumberInt:
                            total = item + total
                    return total
                else:
                    raise StockException('StockRepository', 'AddAllStockInWarehouse', 'Warehouse number must be between 1 and 4.')
            else:
               raise StockException('StockRepository', 'AddAllStockInWarehouse', 'Warehouse number must be an integer.')

        except StockException as error:
            print error
