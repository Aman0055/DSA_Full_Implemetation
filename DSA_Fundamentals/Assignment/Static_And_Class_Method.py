"""
4. Explain and demonstrate `@staticmethod` vs `@classmethod` vs instance methods using a 
`MathUtils` or `Employee` class example.
"""

class solution:
    #Instance Method
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        return f"Employees Name : {self.name}, Salary : {self.salary}"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def create_employee(cls, name , salary):
        return cls(name, salary)

obj1 = solution.create_employee("Aman", 50000)
print(obj1.display())
obj2 = solution("Aditya", 6000000)
print(obj2.display())
obj3 = solution.add(10,20)
print(f"Addition of two numbers : {obj3}")

    