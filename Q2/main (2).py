class Vehicle:
    color = "Gray"
    def __init__(self, name, passengers):
        self.name  = name
        self.passengers = passengers
    def move(self):
        print("Vehicle", self.color, self.name, "is moving")
        print("It has", self.passengers, "passengers")

class Car(Vehicle):
    def move(self):
        print("The car", self.color, self.name, "is travelling along the road")
        print("It has", self.passengers, "passengers")
        
class Boat(Vehicle):
    def move(self):
        print("The boat", self.color, self.name, "is sailing along the water")
        print("It has", self.passengers, "passengers")

class Skateboard:
    def move(self):
        print("The skateboard is moving")
    
car1 = Car("Toyota Altis", 5)
car1.color = "Red"
car2 = Car("BYD Sealion 5", 5)
car2.color = "Blue"
boat = Boat("Yacht", 10)
boat.color = "White"
skbd = Skateboard()

vehicles = [car1, car2, boat, skbd]

for v in vehicles:
    v.move()