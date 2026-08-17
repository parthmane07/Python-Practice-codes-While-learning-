class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        A = self.lenght * self.width
        return A

    def perimeter(self):
        P = 2 * (self.lenght + self.width)
        return P

rec1 = Rectangle(5, 10)
rec2 = Rectangle(20, 50)

print("REC1 Area:", rec1.area())
print("REC1 Perimeter", rec1.perimeter())

print("REC2 Area:", rec2.area())
print("REC2 Perimeter", rec2.perimeter())