'''Imports'''
from datetime import datetime
from StockExceptionClass import StockException

'''Classes'''

class StockItem(object):
    stockItemCount = 0
    pricePerUnitCount = 0.0
    
    def __init__(self, clientNameStr, warehouseNumberInt, pricePerUnitFloat=0.0):
        try:
            print 'Creating a StockItem'

            # Set the uniqueID
            self.uniqueID = StockItem.stockItemCount
            
            # Set the clientName
            if isinstance(clientNameStr, str) == True:
                self.__clientName = clientNameStr
            else:
                raise StockException('StockItem', '__init__', datetime.now(), 'Client name must be a string.')
                
            # Set the pricePerUnit
            if isinstance(pricePerUnitFloat, float) == True or isinstance(pricePerUnitFloat, int) == True:
                if pricePerUnitFloat >= 0 :
                    self.pricePerUnit = pricePerUnitFloat
                else:
                    raise StockException('StockItem', '__init__', datetime.now(), 'Price per unit can not be set to a negative value.')
            else:
                raise StockException('StockItem', '__init__', datetime.now(), 'Price per unit must be a float.')
        
            # Sets the warehouseNumber        
            if isinstance(warehouseNumberInt, int) == True:
                if 0 < warehouseNumberInt < 5:
                    self.warehouseNumber = warehouseNumberInt
                else:
                    raise StockException('StockItem', '__init__', datetime.now(), 'Warehouse number must be between 1 and 4.')
            else:
                raise StockException('StockItem', '__init__', datetime.now(), 'Warehouse number must be an integer.')
            
            # Add one to the stockItemCount
            StockItem.stockItemCount += 1
            
            
            # Add the item's pricePerUnit to the pricePerUnitCount
            StockItem.pricePerUnitCount += self.pricePerUnit
            
        except StockException as error:
            print error
        
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
