'''Imports'''
from StockItemClass import StockItem

'''Classes'''
class Book(StockItem):
    def __init__(self, titleStr, dateStr, genreStr, authorStr, clientNameStr, warehouseNumberInt, pricePerUnitFloat):
        print 'Creating a book'
        StockItem.__init__(self, clientNameStr, warehouseNumberInt, pricePerUnitFloat)
        self.title = titleStr
        self.dateReleased = dateStr
        self.genre = genreStr
        self.author = authorStr

    def __str__(self):
        print 'Printing book information'
        BookDescription = "Stock ID: %d, Price Per Unit: %f, Warehouse Number: %d \n Title: %s, Release Date: %s, Genre: %s, Author: %s" % (self.uniqueID, self.pricePerUnit, self.warehouseNumber, self.title, self.GetDateReleased(), self.genre, self.author)
        return BookDescription
    
    def GetDateReleased(self):
        print 'Getting book release date'
        pass
    
    def IsAPreRelease(self):
        print 'Checking if book is a pre-release'
        pass
    
    def CalculateStorageCost(self):
        print 'Calculating book storage cost'
        storageCost = (self.pricePerUnit * 0.05) + 1
        return storageCost
