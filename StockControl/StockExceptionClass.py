'''Classes'''

class StockException(Exception):
    
    def __init__(self, errorClassStr, errorMethodStr, errorTimeStr, errorDescriptionStr):
        self.errorClass = errorClassStr
        self.errorMethod = errorMethodStr
        self.errorTime = errorTimeStr
        self.errorDescription = errorDescriptionStr
    
    def __str__(self):
        return '\n*****\nAn exception has occurred! \nClass: %s \nMethod: %s \nTime: %s \nDescription: %s\n*****\n' % (self.errorClass, self.errorMethod, self.errorTime, self.errorDescription)
    
'''
typeError

when an attempt is made to insert a stock item that already exists (i.e insert a stock item where the uniqueID already exists)
when an attempt is made to delete a stock item that does not exist
when an attempt is made to set the stock price value to a negative value
when the genre (as defined above ) is not one of the defined genres (e.g rock, metal, blues)


'''