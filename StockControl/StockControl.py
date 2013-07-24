'''Imports'''

'''Classes'''

class StockItem(object):
    self.stockItemCount = 0
    self.pricePerUnitCount = 0.0
    
    def __init__(self, clientNameStr, pricePerUnitFloat=0.0, warehouseNumberInt):
        self.uniqueID = (self.stockItemCount)
        self.__clientName = clientNameStr
        self.pricePerUnit = pricePerUnitFloat
        self.warehouseNumber = warehouseNumberInt
        self.stockItemCount += 1
        self.pricePerUnitCount += pricePerUnitFloat
        
    def __str__(self):
        stockDescription = "Stock ID: %s, Price Per Unit: %s, Warehouse Number: %s" % self.uniqueID, self.pricePerUnit, self.warehouseNumber
    
    def __add__(self, stockItem1, stockItem2):
        totalPrice = stockItem1.pricePerUnit + stockItem2.pricePerUnit
        return totalPrice
    
    def __mul__(self, stockItem, amountInt):
        totalPrice = stockItem.pricePerUnit * amountInt
        return totalPrice
    
    def CalculateStorageCost(self, stockItem):
        storageCost = stockItem.pricePerUnit * 0.05
        return storageCost


class CD(StockItem):
    def __init__(self):
        self.title
        self.dateReleased
        self.genre
        self.artist
    
    def __str__(self):
        pass
    
    def GetDateReleased(self):
        pass
    
    def IsAPreRelease(self):
        pass
    
    
class Book(StockItem):
    def __init__(self):
        self.title
        self.dateReleased
        self.genre
        self.author

    def __str__(self):
        pass
    
    def GetDateReleased(self):
        pass
    
    def IsAPreRelease(self):
        pass
    
class StockRepository(object):
    def __init__(self):
        pass
    
    def EnterStock(self):
        pass
    
    def MoveStock(self):
        pass
    
    def DeleteStock(self):
        pass
    
    def AddAllStockInWarehouse(self):
        pass
    
class StockException(Exception):
    def __init__(self):
        pass
    
class TestClass(object):
    def __init__(self):
        pass    


'''Functions'''

'''Main Program'''

def main():
    pass
    
if __name__ == "__main__":
    main()