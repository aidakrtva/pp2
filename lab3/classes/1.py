class something:
    def __init__(self, string1):
        self.string1 = string1

    def getString (self):
        self.string1 = string1
    
    def printString (self):
        print ( self.string1.upper())

string = something(str(input()) )
string.printString()
