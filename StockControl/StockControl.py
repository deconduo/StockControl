'''Imports'''

'''Classes'''

class StockItem(object):
    stockItemCount = 0
    pricePerUnitCount = 0.0
    
    def __init__(self, clientNameStr, warehouseNumberInt, pricePerUnitFloat=0.0):
        self.uniqueID = StockItem.stockItemCount
        self.__clientName = clientNameStr
        self.pricePerUnit = pricePerUnitFloat
        self.warehouseNumber = warehouseNumberInt
        StockItem.stockItemCount += 1
        StockItem.pricePerUnitCount += pricePerUnitFloat
        
    def __str__(self):
        stockDescription = "Stock ID: %s, Price Per Unit: %s, Warehouse Number: %s" % (self.uniqueID, self.pricePerUnit, self.warehouseNumber)
        return stockDescription
    
    def __add__(self, stockItem):
        totalPrice = self.pricePerUnit + stockItem.pricePerUnit
        return totalPrice
    
    def __mul__(self, amountInt):
        totalPrice = self.pricePerUnit * amountInt
        return totalPrice
    
    def CalculateStorageCost(self):
        storageCost = self.pricePerUnit * 0.05
        return storageCost


class CD(StockItem):
    def __init__(self, titleStr, dateStr, genreStr, artistStr, clientNameStr, warehouseNumberInt, pricePerUnitFloat):
        StockItem.__init__(self, clientNameStr, warehouseNumberInt, pricePerUnitFloat)
        self.title = titleStr
        self.dateReleased = dateStr
        self.genre = genreStr
        self.artist = artistStr
    
    def __str__(self):
        CDDescription = "Stock ID: %s, Price Per Unit: %s, Warehouse Number: %s \n Title: %s, Release Date: %s, Genre: %s, Artist: %s" % (self.uniqueID, self.pricePerUnit, self.warehouseNumber, self.title, self.GetDateReleased(), self.genre, self.artist)
        return CDDescription
    
    def GetDateReleased(self):
        dateStr = self.dateReleased
        return dateStr
    
    def IsAPreRelease(self):
        pass
    
    def __mul__(self, amountInt):
        totalPrice = self.pricePerUnit * amountInt
        return (totalPrice * 0.9)
    
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
    
    def CalculateStorageCost(self):
        storageCost = (self.pricePerUnit * 0.05) + 1
        return storageCost
        
class StockRepository(object):
    stockCollection
    
    def __init__(self):
        pass
    
    def EnterStock(self, stockItem):
        pass
    
    def MoveStock(self, uniqueIDs, warehouseNumberInt):
        pass
    
    def DeleteStock(self, uniqueIDs):
        pass
    
    def AddAllStockInWarehouse(self, warehouseNumberInt):
        pass
    
class StockException(Exception):
    def __init__(self):
        pass
    
class TestClass(object):
    '''
    Create 5 dvd stock items and 5 book stock items to be added to your stock control system
    Calculate the total holding cost for all 10  stock items created
    Add these items to the stockRepository
    Move and delete the items in the stockRepository
    '''

    def __init__(self):
        pass    


'''Functions'''

'''Main Program'''

def main():
    myItem = StockItem("John", 1, 1.5)
    print myItem
    myItem2 = StockItem("Mary", 2, 5)
    print myItem2
    print myItem+myItem2
    print myItem*2
    myCD = CD("Title", "20/3/2013", "Rock", "Queen", "Mike", 4, 5)
    print myCD
    print myCD * 3
    print myCD + myItem
    print myCD*10
    print myItem2*10
    
if __name__ == "__main__":
    main()