'''Imports'''
from StockItemClass import StockItem

'''Classes'''
class CD(StockItem):
    def __init__(self, titleStr, dateStr, genreStr, artistStr, clientNameStr, warehouseNumberInt, pricePerUnitFloat):
        print 'Creating a CD'
        StockItem.__init__(self, clientNameStr, warehouseNumberInt, pricePerUnitFloat)
        self.title = titleStr
        self.dateReleased = dateStr 
        self.genre = genreStr
        self.artist = artistStr
    
    def __str__(self):
        print 'Printing CD information'
        CDDescription = "Stock ID: %d, Price Per Unit: %f, Warehouse Number: %d \n Title: %s, Release Date: %s, Genre: %s, Artist: %s" % (self.uniqueID, self.pricePerUnit, self.warehouseNumber, self.title, self.GetDateReleased(), self.genre, self.artist)
        return CDDescription
    
    def GetDateReleased(self):
        print 'Getting CD release date'
        dateStr = self.dateReleased
        return dateStr
    
    def IsAPreRelease(self):
        print 'Checking if CD is a pre-release'
        pass
    
    def __mul__(self, amountInt):
        print 'Calculating CD discount'
        totalPrice = self.pricePerUnit * amountInt
        return (totalPrice * 0.9)
