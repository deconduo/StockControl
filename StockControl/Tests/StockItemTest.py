import unittest
from ..Classes.StockItemClass import StockItem

class StockItemTest(unittest.TestCase):
    def setUp(self):
        self.testItem1 = StockItem("Test Client 1", 1, 10.00)
        self.testItem2 = StockItem("Test Client 2", 2, 12.35)

    def tearDown(self):
        pass

    def testAddItems(self):
        self.testAdd = self.testItem1 + self.testItem2
        self.assertEqual(self.testAdd, 22.35)

    def testMultItem(self):
        self.testMult = self.testItem1 * 5
