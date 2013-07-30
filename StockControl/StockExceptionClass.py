'''Classes'''

class StockException(Exception):
    
    def __init__(self, errorClass, errorMethod, errorTime, errorDescription):
        self.errorClassStr = errorClass
        self.errorMethodStr = errorMethod
        self.errorTimeStr = errorTime
        self.errorDescriptionStr = errorDescription
    
    def __str__(self):
        return '\n*****\nAn exception has occurred in \nClass: %s \nMethod: %s \nTime: %s \nDescription: %s\n*****\n' % (self.errorClassStr, self.errorMethodStr, self.errorTimeStr, self.errorDescriptionStr)
    
'''
typeError

when an attempt is made to add/move a stock item to a warehouse  number that is less than 0 or greater than 4
when an attempt is made to insert a stock item that already exists (i.e insert a stock item where the uniqueID already exists)
when an attempt is made to delete a stock item that does not exist
when an attempt is made to set the stock price value to a negative value
when the genre (as defined above ) is not one of the defined genres (e.g rock, metal, blues)


'''