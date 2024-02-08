class Shape:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width 

    def area (self):
        pass


class Rectangle (Shape):
    def area (self):
        self.area = self.lenght * self.width
        print (self.area)

shape1 = Rectangle (int(input()), int (input()))
shape1.area()