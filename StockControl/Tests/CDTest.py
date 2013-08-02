import unittest
from ..Classes.CDClass import CD
from ..Classes.StockExceptionClass import StockException

class CDTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Tests the __str__ function
    def testStr(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.assertEqual(self.testCD1.__str__(), "----------\n" + super(CD, self.testCD1).__str__() + "\n Title: %s, Release Date: %s, Genre: %s, Artist: %s\n----------" % (self.testCD1.title, self.testCD1.GetDateReleased(), self.testCD1.genre, self.testCD1.artist))

    # Tests that the title must be a string. Gives an array instead, and tests for an exception.
    def testInitTitleException1(self):
        self.assertRaises(StockException, CD, [], "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        
    # Tests that the title must be less than 100 characters. Gives a long title instead, and tests for an exception.
    def testInitTitleException2(self):
        self.assertRaises(StockException, CD, "Extra long title -------------------------------------------------------------------------------------", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        
    # Tests that the date is in a valid format. Gives a bad date instead, and tests for an exception.
    def testInitDateException(self):
        self.assertRaises(StockException, CD, "Test CD 1", "50/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        
    # Tests that the genre must be a string. Gives an array instead, and tests for an exception.
    def testInitGenreException1(self):
        self.assertRaises(StockException, CD, "Test CD 1", "1/3/2013", [], "Test Artist 1", "Test Client 1", 1, 11.00)
        
    # Tests that the genre must be either Rock, Metal or Blues. Gives Jazz instead, and tests for an exception.
    def testInitGenreException2(self):
        self.assertRaises(StockException, CD, "Test CD 1", "1/3/2013", "Jazz", "Test Artist 1", "Test Client 1", 1, 11.00)
        
    # Tests that the artist must be a string. Gives an array instead, and tests for an exception.
    def testInitArtistException(self):
        self.assertRaises(StockException, CD, "Test CD 1", "1/3/2013", "Rock", [], "Test Client 1", 1, 11.00)
    
    # Tests the GetDateReleased method   
    def testDateReleased(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.assertEqual(self.testCD1.GetDateReleased(), "01/March/2013")

    # Tests the isAPreRelease method
    def testPreRelease(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testCD2 = CD("Test CD 2", "1/3/2014", "Metal", "Test Artist 2", "Test Client 2", 2, 12.00)
        self.assertEqual(self.testCD1.IsAPreRelease(), False)
        self.assertEqual(self.testCD2.IsAPreRelease(), True)
        
        # Tests multiply method is working.
    def testMultItem(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testMult = self.testCD1 * 5
        self.assertEqual(self.testMult, 49.50)
    
    # Tests multiply method works only with integers. Gives a float instead, and tests for an exception.
    def testMultException(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        with self.assertRaises(StockException):
            self.testCD1 * 5.5

