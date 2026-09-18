class Car: 
    def __init__(self, brand, model, battery=35):
        self.brand = brand
        self.model = model
        self.__battery = battery
        self.__odometer = 0
    def go(self, distance):
        self.__battery -= distance/20
        self.__odometer += distance
        print("The car traveled",distance,"km")
        print("You have",self.__battery,"wH left")
    def charge(self, wH):
        self.__battery += wH
        print("Car recharged. You now have",self.__battery,"wH")
    def dashboard(self):
        print("Battery:",self.__battery,"wH")
        print("Odometer:",self.__odometer,"KM")
mycar = Car("BYD","Seal 5")
mycar.battery += 5
