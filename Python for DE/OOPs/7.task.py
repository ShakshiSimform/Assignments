class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def save_to_file(self):
        with open(f"{self.brand}_{self.model}.txt", "w") as file:
            file.write(f"Brand: {self.brand}\n")
            file.write(f"Model: {self.model}\n")
            file.write(f"Year: {self.year}\n")
            file.write(f"Price: {self.price}\n")

# Create object and save to file
vehicle = Vehicle("Toyota", "Camry", 2021, 25000)
vehicle.save_to_file()
