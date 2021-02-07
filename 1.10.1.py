import math


class Rectangle:
    width, length = None, None

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.length * self.width

    def __str__(self):
        return f"{self.__class__.__name__} ({self.width}, {self.length})"


class Square(Rectangle):
    width = None

    def __init__(self, width):
        self.width = width

    def get_area(self):
        return self.width ** 2

    def __str__(self):
        return f"{self.__class__.__name__} ({self.width})"


class Circle:
    radius = None

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return round(2 * math.pi * self.radius ** 2, 4)

    def __str__(self):
        return f"{self.__class__.__name__} ({self.radius})"


rect_1 = Rectangle(10, 2)
rect_2 = Rectangle(5, 3)
square_1 = Square(4)
circle_1 = Circle(3)

figures = [rect_1, rect_2, square_1, circle_1]
for fig in figures:
    print(f"{fig}. Area = {fig.get_area()}")
