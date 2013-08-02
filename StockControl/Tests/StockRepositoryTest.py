'''Imports'''
import unittest
from ..Classes.StockRepositoryClass import StockRepository
from ..Classes.CDClass import CD
from ..Classes.StockExceptionClass import StockException

'''Classes'''
class StockRepositoryTest(unittest.TestCase):
    
    # Creates a new repository for each test
    def setUp(self):
        self.testRepository = StockRepository()

    def tearDown(self):
        pass
    
    # Tests initialisation method
    def testInit(self):
        self.assertEqual(self.testRepository.stockCollection, {})
    
    # Tests __str__ method
    def testStr(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertEqual(self.testRepository.__str__(), str(self.testRepository.stockCollection[self.testCD1.uniqueID]) + "\n")

    # Tests EnterStock method
    def testEnterStock(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertEqual(self.testRepository.stockCollection[self.testCD1.uniqueID], self.testCD1)
        
    # Tests EnterStock exception when item already exists in repository
    def testEnterStockException(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.EnterStock, self.testCD1)
        
    # Tests MoveStock method for a single uniqueID
    def testMoveStock1(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.testRepository.MoveStock(self.testCD1.uniqueID, 2)
        self.assertEqual(self.testCD1.warehouseNumber, 2)
    
    # Tests MoveStock method for a list of uniqueIDs
    def testMoveStock2(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testCD2 = CD("Test CD 2", "2/3/2013", "Metal", "Test Artist 2", "Test Client 2", 2, 12.00)
        self.testRepository.EnterStock(self.testCD1)
        self.testRepository.EnterStock(self.testCD2)
        self.testRepository.MoveStock([self.testCD1.uniqueID, self.testCD1.uniqueID],  2)
        self.assertEqual(self.testCD1.warehouseNumber, 2)

    # Tests MoveStock exception where a non-integer warehouseNumber is given 
    def testMoveStockException1(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.MoveStock, self.testCD1.uniqueID, 1.5)
    
    # Tests MoveStock exception where a warehouseNumber not between 1 and 4 is given 
    def testMoveStockException2(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.MoveStock, self.testCD1.uniqueID, 5)
    
    # Tests MoveStock exception where a non-integer uniqueID is given 
    def testMoveStockException3(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.MoveStock, 9.5, 2)
    
    # Tests MoveStock exception where a uniqueID not in the repository is given 
    def testMoveStockException4(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.MoveStock, 99999, 2)
    
    # Tests MoveStock exception where a uniqueID in a list not in the repository is given    
    def testMoveStockException5(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.MoveStock, [self.testCD1.uniqueID, 99999], 2)
    
    # Tests the DeleteStock method for a single uniqueID
    def testDeleteStock1(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.testRepository.DeleteStock(self.testCD1.uniqueID)
        self.assertEqual(self.testRepository.stockCollection, {})
        
    # Tests the DelteStock method for a list of uniqueIDs
    def testDeleteStock2(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testCD2 = CD("Test CD 2", "2/3/2013", "Metal", "Test Artist 2", "Test Client 2", 2, 12.00)
        self.testRepository.EnterStock(self.testCD1)
        self.testRepository.EnterStock(self.testCD2)
        self.testRepository.DeleteStock([self.testCD1.uniqueID, self.testCD2.uniqueID])
        self.assertEqual(self.testRepository.stockCollection, {})
    
    # Tests DeleteStock exception where a non-integer uniqueID is given
    def testDeleteStockException1(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.DeleteStock, 1.5)
    
    # Tests DeleteStock exception where a uniqueID not in the repository is given
    def testDeleteStockException2(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.DeleteStock, 9999)
    
    # Tests DeleteStock exception where a uniqueID in a list not in the repository is given
    def testDeleteStockException3(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.DeleteStock, [self.testCD1, 9999])
    
    # Tests the AddAllStock method
    def testAddAllStock(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testCD2 = CD("Test CD 2", "2/3/2013", "Metal", "Test Artist 2", "Test Client 2", 1, 12.00)
        self.testRepository.EnterStock(self.testCD1)
        self.testRepository.EnterStock(self.testCD2)
        self.addStock = self.testRepository.AddAllStockInWarehouse(1)
        self.assertEqual(self.addStock, 23.00)
    
    # Tests AddAllStock exception where a non-integer warehouseNumber is given
    def testAddAllStockException1(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.AddAllStockInWarehouse, 1.5)
        
    # Tests AddAllStock exception where a warehouseNumber not between 1 and 4 is given
    def testAddAllStockException2(self):
        self.testCD1 = CD("Test CD 1", "1/3/2013", "Rock", "Test Artist 1", "Test Client 1", 1, 11.00)
        self.testRepository.EnterStock(self.testCD1)
        self.assertRaises(StockException, self.testRepository.AddAllStockInWarehouse, 5)