class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")

class Car(Vehicle):
    def display_info(self):
        print(f"Car - Model: {self.model}, Price: {self.price}")

class Bike(Vehicle):
    def display_info(self):
        print(f"Bike - Model: {self.model}, Price: {self.price}")

# Demonstrate Polymorphism
vehicle = Vehicle("Toyota", "Camry", 2021, 25000)
car = Car("Honda", "Civic", 2022, 22000)
bike = Bike("Yamaha", "FZ", 2021, 12000)

for v in [vehicle, car, bike]:
    v.display_info()
