'''Imports'''
from datetime import datetime
from StockItemClass import StockItem
from StockExceptionClass import StockException

'''Classes'''
class Book(StockItem):
    def __init__(self, titleStr, dateStr, genreStr, authorStr, clientNameStr, warehouseNumberInt, pricePerUnitFloat):
        print 'Creating a book'
        # Initialise the StockItem class.
        StockItem.__init__(self, clientNameStr, warehouseNumberInt, pricePerUnitFloat)
        
        # Sets the title, test to make sure its a string and is less than 100 characters.
        try:
            if isinstance(titleStr, str) == True:
                if len(titleStr) <= 100:
                    self.title = titleStr
                else:
                    self.title = titleStr[:100]
                    raise StockException('Book', '__init__', 'Title must be less than 100 characters. Title has been truncated.')
            else:
                self.title = 'Book Title'
                raise StockException('Book', '__init__', 'Title must be a string. Value has been set to a default title.')
        except StockException as error:
            print error   
            
        # Sets the dateReleased, tests to make sure date is in a valid format.
        try:
            try:
                self.dateReleased = datetime.strptime(dateStr, "%d/%m/%Y")
            
            except ValueError:
                self.dateReleased = datetime.now()
                raise StockException('Book', '__init__', 'Date must be in the format DD/MM/YYYY. A default date has been set.')
        except StockException as error:
            print error    
        # Sets the genre, tests to make sure its a string and a valid genre.
        try:
            if isinstance(genreStr, str) == True:
                if genreStr in ['Rock', 'Metal', 'Blues']:
                    self.genre = genreStr
                else:
                    self.genreStr = 'Rock'
                    raise StockException('Book', '__init__', 'Genre must be either Rock, Metal or Blues. Value has been set to a default genre.')
            else:
                self.genreStr = 'Rock'
                raise StockException('Book', '__init__', 'Genre must be a string. Value has been set to a default genre.')
        except StockException as error:
            print error   

        # Sets the artist, tests to make sure its a string.
        try:
            if isinstance(authorStr, str) == True:
                self.author = authorStr
            else:
                self.author = 'Book Author'
                raise StockException('Book', '__init__', 'Author must be a string. Value has been set to a default author.')
        except StockException as error:
            print error
    
    # Prints information about the book.
    def __str__(self):
        print 'Printing book information'
        BookDescription = "----------\n" + super(Book, self).__str__() + "\n Title: %s, Release Date: %s, Genre: %s, Author: %s\n----------" % (self.title, self.GetDateReleased(), self.genre, self.author)
        return BookDescription
    
    # Returns the dateReleased in the format DD/MonthName/YYYY.
    def GetDateReleased(self):
        print 'Getting book release date'
        dateStr = datetime.strftime(self.dateReleased, "%d/%B/%Y")
        return dateStr
    
    # Returns True if dateReleased is in the future.
    def IsAPreRelease(self):
        print 'Checking if book is a pre-release'
        return self.dateReleased > datetime.now()
    
    # Higher storage cost for books
    def CalculateStorageCost(self):
        print 'Calculating book storage cost'
        storageCost = (self.pricePerUnit * 0.05) + 1
        return storageCost
