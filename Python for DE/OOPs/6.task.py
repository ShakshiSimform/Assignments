class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def calculate_discount(self, percentage, additional_discount=0):
        if additional_discount:
            discount_price = self.price * (1 - percentage / 100) * (1 - additional_discount / 100)
        else:
            discount_price = self.price * (1 - percentage / 100)
        return discount_price

# Demonstrate method overloading
vehicle = Vehicle("Toyota", "Camry", 25000)
print(f"Discounted Price (Single): {vehicle.calculate_discount(10)}")
print(f"Discounted Price (Double): {vehicle.calculate_discount(10, 5)}")
