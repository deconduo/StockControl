'''Imports'''

'''Classes'''

class StockItem(object):
    self.runningTotal = 0
    def __init__(self, clientNameStr, pricePerUnitFloat=0.0, warehouseNumberInt):
        self.uniqueID = (self.runningTotal)
        self.__clientName = clientNameStr
        self.pricePerUnit = pricePerUnitFloat
        self.warehouseNumber = warehouseNumberInt
        self.runningTotal += 1
    def __str__(self):
        pass
    
    def stockAdd(self):
        pass
    
    def stockMultiply(self):
        pass
    
    def CalculateStorageCost(self):
        pass


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