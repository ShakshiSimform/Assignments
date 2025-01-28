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
    def __init__(self, brand, model, year, price, number_of_doors):
        super().__init__(brand, model, year, price)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.number_of_doors}")

# Create object and call display_info
car = Car("Toyota", "Corolla", 2022, 22000.00, 4)
car.display_info()
