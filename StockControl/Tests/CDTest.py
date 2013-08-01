import unittest
from ..Classes.CDClass import CD

class CDTest(unittest.TestCase):
    def setUp(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testCD2 = CD("Test CD 2", "2/3/2014", "Metal", "Test Artist 2", "Test Client 2", 2, 12.00)

    def tearDown(self):
        pass

    def testAddItems(self):
        self.testAdd = self.testCD1 + self.testCD2
        self.assertEqual(self.testAdd, 23.00)
        
    def testPreRelease(self):
        self.assertEqual(self.testCD1.IsAPreRelease(), False)
        self.assertEqual(self.testCD2.IsAPreRelease(), True)

