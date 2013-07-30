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