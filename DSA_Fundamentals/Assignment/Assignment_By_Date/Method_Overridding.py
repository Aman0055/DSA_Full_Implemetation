"""
1. Implement method overriding: create a base class `Shape` with a method `area()` that
 returns 0, and derived classes `Circle` and `Square` that override `area()` correctly.
"""

class Shape:

    def area(self):
        return None

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):

    def __init__(self, base, perpendicular):
        self.base = base
        self.perpendicular = perpendicular

    def area(self):
        return 0.5 * self.base * self.perpendicular

shapes = [Circle(5), Square(4), Shape(), Triangle(12, 4)]

for shape in shapes:
    print(f"{type(shape).__name__}, area : {shape.area()}")