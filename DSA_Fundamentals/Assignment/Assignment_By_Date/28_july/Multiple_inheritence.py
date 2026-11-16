"""
2. Demonstrate multiple inheritance with a `Flyable` class and `Swimmable` class, 
combined into a `Duck` class. Explain how Python resolves the Method Resolution Order (MRO).
"""
class Flyable:

    def fly(self):
        return "I can fly"

class Swimmable:

    def swim(self):
        return "I can swim"

class Duck(Flyable , Swimmable):

    def quack(self):
        return "Quark"

d = Duck()
print(d.fly())
print(d.swim())
print(d.quack())