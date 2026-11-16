"""
3. Create an abstract class `Vehicle` using the `abc` module with an abstract method
 `fuel_type()`. Implement it in `PetrolCar` and `ElectricCar`.
"""

from abc import ABC , abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def fuel_type(self):
        pass
class PetrolCar(Vehicle):

    def fuel_type(self):
        return "type of fuel : petrol"

class Electric_Car(Vehicle):

    def fuel_type(self):
        return "type of fuel : electricity"

for obj in [PetrolCar() , Electric_Car()]:
    print(f"{type(obj).__name__} : {obj.fuel_type()}")