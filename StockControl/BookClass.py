from StockItemClass import StockItem

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
