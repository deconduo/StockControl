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
        stockDescription = "Stock ID: %d, Price Per Unit: %f, Warehouse Number: %d" % (self.uniqueID, self.pricePerUnit, self.warehouseNumber)
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
        CDDescription = "Stock ID: %d, Price Per Unit: %f, Warehouse Number: %d \n Title: %s, Release Date: %s, Genre: %s, Artist: %s" % (self.uniqueID, self.pricePerUnit, self.warehouseNumber, self.title, self.GetDateReleased(), self.genre, self.artist)
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
    def __init__(self, titleStr, dateStr, genreStr, authorStr, clientNameStr, warehouseNumberInt, pricePerUnitFloat):
        StockItem.__init__(self, clientNameStr, warehouseNumberInt, pricePerUnitFloat)
        self.title = titleStr
        self.dateReleased = dateStr
        self.genre = genreStr
        self.author = authorStr

    def __str__(self):
        BookDescription = "Stock ID: %d, Price Per Unit: %f, Warehouse Number: %d \n Title: %s, Release Date: %s, Genre: %s, Author: %s" % (self.uniqueID, self.pricePerUnit, self.warehouseNumber, self.title, self.GetDateReleased(), self.genre, self.author)
        return BookDescription
    
    def GetDateReleased(self):
        pass
    
    def IsAPreRelease(self):
        pass
    
    def CalculateStorageCost(self):
        storageCost = (self.pricePerUnit * 0.05) + 1
        return storageCost
        
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
        pass
    
class StockException(Exception):
    def __init__(self):
        pass
    
class TestClass(object):
    def test(self):
        testCD1 = CD("Test CD 1", "20/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 10.00)
        testCD2 = CD("Test CD 2", "20/3/2013", "Metal", "Test Artist 2", "Test Client 2", 1, 15.50)
        testCD3 = CD("Test CD 3", "20/3/2013", "Blues", "Test Artist 3", "Test Client 3", 2, 22.32)
        testCD4 = CD("Test CD 4", "20/3/2013", "Rock", "Test Artist 4", "Test Client 4", 1, 12.10)
        testCD5 = CD("Test CD 5", "20/3/2013", "Metal", "Test Artist 5", "Test Client 5", 1, 9.40)
        testBook1 = Book("Test Book 1", "20/3/2013", "Crime", "Test Author 1", "Test Client 6", 4, 4.30)
        testBook2 = Book("Test Book 2", "20/3/2013", "Drama", "Test Author 2", "Test Client 7", 3, 9.99)
        testBook3 = Book("Test Book 3", "20/3/2013", "Science Fiction", "Test Author 3", "Test Client 8", 4, 3.95)
        testBook4 = Book("Test Book 4", "20/3/2013", "Crime", "Test Author 4", "Test Client 9", 4, 6.78)
        testBook5 = Book("Test Book 5", "20/3/2013", "Drama", "Test Author 5", "Test Client 10", 3, 15.20)
        newStock = [testCD1, testCD2, testCD3, testCD4, testCD5, testBook1, testBook2, testBook3, testBook4, testBook5]
        
        total = 0
        for stockItem in newStock:
            total += stockItem.CalculateStorageCost()
        print "Total holding price: %s" % (total)
        
        testRepository = StockRepository()
        for stockItem in newStock:
            testRepository.EnterStock(stockItem)
        
        print testRepository
        
        for stockItem in newStock:
            testRepository.MoveStock(stockItem.uniqueID, 3)
           
        print testRepository

         
        for stockItem in newStock:
            testRepository.DeleteStock(stockItem.uniqueID)
            
        print testRepository

    '''
    Move and delete the items in the stockRepository
    '''

    def __init__(self):
        pass    


'''Functions'''

'''Main Program'''

def main():
    myTest = TestClass()
    myTest.test()
    
if __name__ == "__main__":
    main()