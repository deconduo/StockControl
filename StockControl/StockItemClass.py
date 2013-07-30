'''Imports'''
from datetime import datetime
from StockExceptionClass import StockException

'''Classes'''

class StockItem(object):
    stockItemCount = 0
    pricePerUnitCount = 0.0
    
    def __init__(self, clientNameStr, warehouseNumberInt, pricePerUnitFloat=0.0):
        print 'Creating a StockItem'
        self.uniqueID = StockItem.stockItemCount
        self.__clientName = clientNameStr
        if isinstance(pricePerUnitFloat, float) == True:
            if pricePerUnitFloat > 0 :
                self.pricePerUnit = pricePerUnitFloat
            else:
                raise StockException('StockItem', '__init__', datetime.now().time(), 'Price per unit can not be set to a negative value. Defaulting to 0')
                self.pricePerUnit = 0
        else:
            raise StockException('StockItem', '__init__', datetime.now().time(), 'Price per unit must be a float. Defaulting to 0')
            self.pricePerUnit = 0
            
        self.warehouseNumber = warehouseNumberInt
        StockItem.stockItemCount += 1
        StockItem.pricePerUnitCount += pricePerUnitFloat
        
    def __str__(self):
        print 'Printing StockItem information'
        stockDescription = "Stock ID: %d, Price Per Unit: %f, Warehouse Number: %d" % (self.uniqueID, self.pricePerUnit, self.warehouseNumber)
        return stockDescription
    
    def __add__(self, stockItem):
        print 'Adding StockItems'
        if isinstance(stockItem, StockItem) == True:
            totalPrice = self.pricePerUnit + stockItem.pricePerUnit
        else:
            totalPrice = self.pricePerUnit + stockItem
        return totalPrice
    
    def __mul__(self, amountInt):
        print 'Multiplying a StockItem'
        totalPrice = self.pricePerUnit * amountInt
        return totalPrice
    
    def CalculateStorageCost(self):
        print 'Calculating storage cost of a StockItem'
        storageCost = self.pricePerUnit * 0.05
        return storageCost
