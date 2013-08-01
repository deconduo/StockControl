'''Imports'''
import unittest
from StockControl.Tests.StockItemTest import StockItemTest
from StockControl.Tests.CDTest import CDTest
from StockControl.Tests.BookTest import BookTest
from StockControl.Tests.StockRepositoryTest import StockRepositoryTest


'''Main Program'''

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(StockItemTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(CDTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(BookTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(StockRepositoryTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()