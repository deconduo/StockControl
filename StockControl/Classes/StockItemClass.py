'''Imports'''
from StockExceptionClass import StockException

'''Classes'''

class StockItem(object):
    # Running count of total number of items
    stockItemCount = 0
    
    # Running count of total price per unit of all items
    pricePerUnitCount = 0.0
    
    # Creates a new StockItem
    def __init__(self, clientNameStr, warehouseNumberInt, pricePerUnitFloat=0.00):
        print 'Creating a StockItem'

        # Set the uniqueID
        self.uniqueID = StockItem.stockItemCount
        
        # Set the clientName, test to make sure it is a string.
        if isinstance(clientNameStr, str) == True:
            self.__clientName = clientNameStr
        else:
            raise StockException('StockItem', '__init__', 'Client name must be a string.')
  
        # Set the pricePerUnit, test to make sure it a non-negative number.
        if isinstance(pricePerUnitFloat, float) == True or isinstance(pricePerUnitFloat, int) == True:
            if pricePerUnitFloat >= 0 :
                self.pricePerUnit = float(pricePerUnitFloat)
            else:
                raise StockException('StockItem', '__init__', 'Price per unit can not be set to a negative value.')
        else:
            raise StockException('StockItem', '__init__', 'Price per unit must be a number.')

        # Sets the warehouseNumber, test to make sure it a number between 1 and 4.      
        if isinstance(warehouseNumberInt, int) == True:
            if 0 < warehouseNumberInt < 5:
                self.warehouseNumber = warehouseNumberInt
            else:
                self.warehouseNumber = 1
                raise StockException('StockItem', '__init__', 'Warehouse number must be between 1 and 4. Value has been set to a default of 1.')
        else:
            self.warehouseNumber = 1
            raise StockException('StockItem', '__init__', 'Warehouse number must be an integer. Value has been set to a default of 1.')
        
        # Add one to the stockItemCount
        StockItem.stockItemCount += 1
        
        
        # Add the item's pricePerUnit to the pricePerUnitCount
        StockItem.pricePerUnitCount += self.pricePerUnit
        

    # Prints information about the item    
    def __str__(self):
        print 'Printing StockItem information'
        stockDescription = "Stock ID: %s, Price Per Unit: %.2f, Warehouse Number: %s" % (self.uniqueID, self.pricePerUnit, self.warehouseNumber)
        return stockDescription
    
    # Adds the pricePerUnit of a StockItem with another, or with a number    
    def __add__(self, stockItem):
        
        # Tests to see if the value passed is a StockItem or a number. If not, raises and exception.
        print 'Adding StockItems'
        if isinstance(stockItem, StockItem) == True:
            totalPrice = self.pricePerUnit + stockItem.pricePerUnit
        elif isinstance(stockItem, float) == True or isinstance(stockItem, int) == True:
            totalPrice = self.pricePerUnit + stockItem
        else:
            raise StockException('StockItem', '__add__', 'Can only add StockItems or numbers.')
        return float(totalPrice)
    
    # Multiplies the pricePerUnit of a StockItem by an integer
    def __mul__(self, amountInt):
        
        # Tests to make sure that an integer has been given. If not, raises an exception.
        print 'Multiplying a StockItem'
        if isinstance(amountInt, int) == True:
            totalPrice = self.pricePerUnit * amountInt
        else:
            raise StockException('StockItem', '__mul__', 'Can only multiply by an integer.')
        return float(totalPrice)

    
    # Calculates the storage cost of an item.
    def CalculateStorageCost(self):
        print 'Calculating storage cost of a StockItem'
        storageCost = self.pricePerUnit * 0.05
        return storageCost
