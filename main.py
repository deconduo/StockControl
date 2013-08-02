'''Imports'''
import unittest
from StockControl.Tests.StockItemTest import StockItemTest
from StockControl.Tests.CDTest import CDTest
from StockControl.Tests.BookTest import BookTest
from StockControl.Tests.StockRepositoryTest import StockRepositoryTest
from StockControl.Tests.StockExceptionTest import StockExceptionTest
from StockControl.Tests.TestClass import TestClass

'''Main Program'''

def main():
    # Run all the unit tests.
    suite = unittest.TestLoader().loadTestsFromTestCase(StockItemTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(CDTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(BookTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(StockRepositoryTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(StockExceptionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    # Run the test class
    myTest = TestClass()
    myTest.test()

if __name__ == "__main__":
    main()