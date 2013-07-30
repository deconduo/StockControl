class StockRepository(object):
    
    def __init__(self):
        self.stockCollection = []
        
    def __str__(self):
        repositoryDesc = ""
        for stockItem in self.stockCollection:
             repositoryDesc += (str(stockItem) + "\n")
        return repositoryDesc
    
    def EnterStock(self, stockItem):
        self.stockCollection.append(stockItem)
    
    def MoveStock(self, uniqueIDs, warehouseNumberInt):
        for stockItem in self.stockCollection:
            if stockItem.uniqueID in uniqueIDs:
                stockItem.warehouseNumber = warehouseNumberInt
    
    def DeleteStock(self, uniqueIDs):
        for stockItem in self.stockCollection:
            if stockItem.uniqueID in uniqueIDs:
                self.stockCollection.remove(stockItem)
    
    def AddAllStockInWarehouse(self, warehouseNumberInt):
        total = 0
        for item in self.stockCollection:
            if item.warehouseNumber == warehouseNumberInt:
                if total == 0:
                    total = item.pricePerUnit
                else:
                    total = item + total
        return total