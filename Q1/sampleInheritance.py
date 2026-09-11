"""INHERITANCE"""
class Vehicle:
    def __init__(self, Kindofvehicle):
        self.Kindofvehicle = Kindofvehicle
        print(self.Kindofvehicle, "created")

    def move(self, distance):
        print(self.Kindofvehicle, "moved", distance, end="")

class Car(Vehicle):
    def __init__(self, Kindofvehicle, brand, model):
        self.brand = brand
        self.model = model
        super().__init__(Kindofvehicle)
        print("It is a", brand, model)
    def move(self, distance):
        super().move(distance)
        print("km")
class Boat(Vehicle):
    def __init__(self, Kindofvehicle, model):
        self.model = model
        super().__init__(Kindofvehicle)
        print("It is a" ,self.model)
    def mode(self, distance):
        super().move(distace)
        print("Nm")
              
vios = Car("car", "Toyota", "Vios")
vios.move(10)
ferry = Boat("ferry", "SuperFerry")
ferry.move(20)
yacht = Boat("yacht", "Subic Yacht")
yacht.move(25)
