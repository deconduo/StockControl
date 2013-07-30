'''Imports'''
from StockExceptionClass import StockException

'''Classes'''
class StockRepository(object):
    
    def __init__(self):
        print 'Creating a StockRepository'
        self.stockCollection = []
        
    def __str__(self):
        print 'Printing StockRepository information'
        repositoryDesc = ""
        for stockItem in self.stockCollection:
             repositoryDesc += (str(stockItem) + "\n")
        return repositoryDesc
    
    def EnterStock(self, stockItem):
        print 'Adding a StockItem to a Repository'
        self.stockCollection.append(stockItem)
    
    def MoveStock(self, uniqueIDs, warehouseNumberInt):
        print 'Moving stock to a new warehouse'
        for stockItem in self.stockCollection:
            if isinstance(uniqueIDs, int) == True:
                if stockItem.uniqueID == uniqueIDs:
                    stockItem.warehouseNumber = warehouseNumberInt
            else:                
                if stockItem.uniqueID in uniqueIDs:
                    stockItem.warehouseNumber = warehouseNumberInt
    
    def DeleteStock(self, uniqueIDs):
        print 'Deleting stock from a warehouse'
        for stockItem in self.stockCollection:
            if isinstance(uniqueIDs, int) == True:
                if stockItem.uniqueID == uniqueIDs:
                    self.stockCollection.remove(stockItem)
            else:
                if stockItem.uniqueID in uniqueIDs:
                    self.stockCollection.remove(stockItem)
    
    def AddAllStockInWarehouse(self, warehouseNumberInt):
        print 'Adding all stock in a warehouse'
        total = 0
        for item in self.stockCollection:
            if item.warehouseNumber == warehouseNumberInt:
                total = item + total
        return total
