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

# Create object and call display_info
vehicle = Vehicle("Toyota", "Camry", 2021, 2500000.00)
vehicle.display_info()

