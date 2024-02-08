class Shape:
    def __init__(self, lenght):
        self.lenght = lenght

    def area (self):
        pass


class Square(Shape):
    def area (self):
        self.area = self.lenght ** 2
        print (self.area)

shape1 = Square(int (input()))
shape1.area()