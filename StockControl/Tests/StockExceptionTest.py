import unittest
from datetime import datetime
from ..Classes.StockExceptionClass import StockException

class StockExceptionTest(unittest.TestCase):
    def setUp(self):
        self.errorClass = "Test Class"
        self.errorMethod = "Test Method"
        self.errorTime = datetime.now().strftime('%H:%M:%S %d/%B/%Y')
        self.errorDescription = "Test Description"

    def tearDown(self):
        pass
    
    def testStr(self):
        try:
            raise StockException(self.errorClass, self.errorMethod, self.errorDescription)
        except StockException as error:
            self.assertEqual(error.__str__(), '\n*****\nAn exception has occurred! \nClass: %s \nMethod: %s \nTime: %s \nDescription: %s\n*****\n' % (self.errorClass, self.errorMethod, self.errorTime, self.errorDescription))
