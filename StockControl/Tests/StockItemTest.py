import unittest
from ..Classes.StockItemClass import StockItem

class StockItemTest(unittest.TestCase):
    def setUp(self):
        self.testItem1 = StockItem("Test Client 1", 1, 11.00)
        self.testItem2 = StockItem("Test Client 2", 2, 12.00)

    def tearDown(self):
        pass

    def testAddItems(self):
        self.testAdd = self.testItem1 + self.testItem2
        self.assertEqual(self.testAdd, 23.00)

    def testMultItem(self):
        self.testMult = self.testItem1 * 5
        self.assertEqual(self.testMult, 55.00)
