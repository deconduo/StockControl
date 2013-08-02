'''Imports'''
from StockExceptionClass import StockException

'''Classes'''
class StockRepository(object):
    
    # Creates an empty array for the storage of StockItems when object is created.
    def __init__(self):
        
        # print 'Creating a StockRepository'
        self.stockCollection = {}
    
    # Prints each StockItem in a readable format.    
    def __str__(self):
        
        # print 'Printing StockRepository information'
        repositoryDesc = ""
        for stockItem in self.stockCollection:
             repositoryDesc += (str(self.stockCollection[stockItem]) + "\n")
        return repositoryDesc
    
    # Adds a StockItem to the Repository, checks to make sure it doesn't exist in there beforehand.
    def EnterStock(self, stockItem):
        
        # print 'Adding a StockItem to a Repository'
        if stockItem.uniqueID not in self.stockCollection:
                self.stockCollection[stockItem.uniqueID] = stockItem
        else:
            raise StockException('StockRepository', 'EnterStock', 'The item you attempted to add already exists in repository.')
        
    # Moves a list of stockItems to a new warehouse. Checks that the uniqueIDs and the warehouseNumber are viable.
    def MoveStock(self, uniqueIDs, warehouseNumberInt):
        
        # print 'Moving stock to a new warehouse'
        if isinstance(warehouseNumberInt, int):
            if 0 < warehouseNumberInt < 5:
                if isinstance(uniqueIDs, int) == True:
                    if uniqueIDs in self.stockCollection:
                        self.stockCollection[uniqueIDs].warehouseNumber = warehouseNumberInt
                    else:
                        raise StockException('StockRepository', 'MoveStock', 'The Unique ID given was not found in repository')
                elif isinstance(uniqueIDs, array) == True:
                    for ID in uniqueIDs:               
                        if ID in self.stockCollection:
                            self.stockCollection[ID].warehouseNumber = warehouseNumberInt
                        else:
                            raise StockException('StockRepository', 'MoveStock', 'At least one Unique ID was not found in repository')
                else:
                    raise StockException('StockRepository', 'MoveStock', 'You must provide either a single uniqueID or an array of uniqueIDs')
            else:
                raise StockException('StockRepository', 'MoveStock', 'Warehouse number must be between 1 and 4.')
        else:
           raise StockException('StockRepository', 'MoveStock', 'Warehouse number must be an integer.')
    
    # Deletes stock from the repository. Checks to make sure the uniqueIDs given are viable.
    def DeleteStock(self, uniqueIDs):
        
        # print 'Deleting stock from repository'
        if isinstance(uniqueIDs, int) == True:
            if uniqueIDs in self.stockCollection:
                del self.stockCollection[uniqueIDs]
            else:
                raise StockException('StockRepository', 'DeleteStock', 'The Unique ID given was not found in repository')
            
        elif isinstance(uniqueIDs, array) == True:
            for ID in uniqueIDs:               
                if ID in self.stockCollection:
                    del self.stockCollection[ID]
                else:
                    raise StockException('StockRepository', 'DeleteStock', 'At least one Unique ID was not found in repository')
        else:
            raise StockException('StockRepository', 'DeleteStock', 'You must provide either a single uniqueID or an array of uniqueIDs')
    
    # Adds up all the stock in a warehouse. Checks that the warehouse number given is viable.
    def AddAllStockInWarehouse(self, warehouseNumberInt):
        
        # print 'Adding all stock in a warehouse'
        if isinstance(warehouseNumberInt, int):
            if 0 < warehouseNumberInt < 5: 
                total = 0
                for ID in self.stockCollection:
                    if self.stockCollection[ID].warehouseNumber == warehouseNumberInt:
                        total = self.stockCollection[ID] + total
                return total
            else:
                raise StockException('StockRepository', 'AddAllStockInWarehouse', 'Warehouse number must be between 1 and 4.')
        else:
           raise StockException('StockRepository', 'AddAllStockInWarehouse', 'Warehouse number must be an integer.')
