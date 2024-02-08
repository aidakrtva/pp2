import math 

class Point:
    def __init__ (self, x , y):
        self.x = x
        self.y = y
    
    def show (self):

        print (f"Coordinates of the point is ({self.x},{self.y})")
    
    def move (self, newx , newy):
        self.newx = newx  
        self.newy = newy 
        print (f"New coordinates of point is ({self.newx},{self.newy})")

    def dist (self):
        self.xx = (self.newx - self.x) ** 2
        self.yy = (self.newy - self.y) ** 2
        self.distan = math.sqrt(self.xx + self.yy)
        print (f"distance between two points is {self.distan}" )

point1 = Point (4, 6)
point1.show()
point1.move(6,8)
point1.dist()
