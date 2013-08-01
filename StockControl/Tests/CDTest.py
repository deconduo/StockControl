import unittest
from ..Classes.CDClass import CD

class CDTest(unittest.TestCase):
    def setUp(self):
        self.testCD1 = CD("Test CD 1", "20/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 10.00)
        self.testCD2 = CD("Test CD 2", "20/3/2013", "Metal", "Test Artist 2", "Test Client 2", 2, 12.35)

    def tearDown(self):
        pass

    def testAddItems(self):
        self.testAdd = self.testItem1 + self.testItem2
        self.assertEqual(self.testAdd, 22.35)

    def testMultItem(self):
        self.testMult = self.testItem1 * 5
