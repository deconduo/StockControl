''' Imports'''
import unittest
from ..Classes.StockItemClass import StockItem
from ..Classes.StockExceptionClass import StockException

'''Classes'''

# Tests for the StockItem Class
class StockItemTest(unittest.TestCase):
    
    # Creates two StockItems for each test.
    def setUp(self):
        self.testItem1 = StockItem("Test Client 1", 1, 11.00)
        self.testItem2 = StockItem("Test Client 2", 2, 12.00)
        
    
    # Resets the StockCount after each test.
    def tearDown(self):
        pass
    
    # Tests the __str__ function
    def testStr(self):
        self.assertEqual(self.testItem1.__str__(), "Stock ID: 22, Price Per Unit: 11.00, Warehouse Number: 1")
    
    # Tests that the clientName must be a string. Gives an array instead, and tests for an exception.
    def testInitClientException(self):
        self.assertRaises(StockException, StockItem, [], 1, 11.00)
    
    # Tests that the warehouseNumber must be a number. Gives a string instead, and tests for an exception.
    def testInitWarehouseException1(self):
        self.assertRaises(StockException, StockItem, "TestClient 1", "Not a warehouse", 11.00)
        
    # Tests that the warehouseNumber must be between 1 and 4. Gives 5 instead, and tests for an exception.
    def testInitWarehouseException2(self):
        self.assertRaises(StockException, StockItem, "TestClient 1", 5, 11.00)
    
    # Tests that the pricePerUnit must be a number. Gives a string instead, and tests for an exception.
    def testInitPriceException1(self):
        self.assertRaises(StockException, StockItem, "Test Client 1", 1, "Not a number")
    
    # Tests that the pricePerUnit must be non-negative. Gives an -10.00 instead, and tests for an exception.
    def testInitPriceException2(self):
        self.assertRaises(StockException, StockItem, "Test Client 1", 1, -10.00)

    # Tests that the addition method is working when adding two stockItems.
    def testAddItems(self):
        self.testAdd = self.testItem1 + self.testItem2
        self.assertEqual(self.testAdd, 23.00)
    
    # Tests that the addition method is working when adding a stockItem to a number.
    def testAddNumber(self):
        self.testAdd = self.testItem1 + 12.00
        self.assertEqual(self.testAdd, 23.00)
        
    # Tests that the addition method works only with numbers and stockItems. Gives a string instead, and tests for an exception.
    def testAddException(self):
        with self.assertRaises(StockException):
            self.testItem1 + "Not a number or stockItem"
    
    # Tests that calculateStorageCost method is working.
    def testCalculateStorageCost(self):
        self.storageCost = self.testItem1.CalculateStorageCost()
        self.assertEqual(self.storageCost, 0.55)

    # Tests multiply method is working.
    def testMultItem(self):
        self.testMult = self.testItem1 * 5
        self.assertEqual(self.testMult, 55.00)
    
    # Tests multiply method works only with integers. Gives a float instead, and tests for an exception.
    def testMultException(self):
        with self.assertRaises(StockException):
            self.testItem1 * 5.5