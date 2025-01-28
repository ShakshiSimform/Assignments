class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price  # Private attribute

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, price):
        self.__price = price

# Create object and use getter/setter
vehicle = Vehicle("Toyota", "Camry", 2021, 2500000.00)
vehicle.set_price(2900000.00)  # Set price using setter
print(vehicle.get_price())    # Get price using getter
