"""
5. Implement operator overloading: create a `Vector` class where `+` adds two vectors and 
`__str__` gives a readable output like `Vector(3, 4)`.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

obj1 = Vector(3,4)
obj2 = Vector(5,6)

print(obj1)
print(obj2)

obj3 = obj1 + obj2
print(obj3)

