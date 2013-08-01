'''Imports'''
from datetime import datetime

'''Classes'''

class StockException(Exception):
    
    def __init__(self, errorClassStr, errorMethodStr, errorDescriptionStr):
        self.errorClass = errorClassStr
        self.errorMethod = errorMethodStr
        self.errorTime = datetime.now().strftime('%H:%M:%S %d/%B/%Y')
        self.errorDescription = errorDescriptionStr
    
    def __str__(self):
        return '\n*****\nAn exception has occurred! \nClass: %s \nMethod: %s \nTime: %s \nDescription: %s\n*****\n' % (self.errorClass, self.errorMethod, self.errorTime, self.errorDescription)