from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

# Create objects and call calculate_area
rectangle = Rectangle(5, 3)
circle = Circle(7)

print(f"Rectangle Area: {rectangle.calculate_area()}")
print(f"Circle Area: {circle.calculate_area()}")
