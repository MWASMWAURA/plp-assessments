# Assignment 1: Inheritance challenge

# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

# Child class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.__storage = storage       # Encapsulated attribute
        self.battery = battery

    def make_call(self, number):
        print(f"Calling {number} from {self.info()}...")

    def get_storage(self):
        return self.__storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
            print(f"Storage updated to {self.__storage}GB")
        else:
            print("Invalid storage size!")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S22", 128, "4500mAh")
phone2 = Smartphone("Apple", "iPhone 14", 256, "4325mAh")

phone1.make_call("0712345678")
print("Storage:", phone1.get_storage())
phone1.set_storage(256)
print("Updated storage:", phone1.get_storage())


# Assignment 2 : Polymorphism challenge
class Vehicle:
    def __init__(self):
        pass

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
