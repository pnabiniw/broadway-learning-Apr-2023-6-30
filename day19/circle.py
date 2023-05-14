# Create a class Circle. Take radius as a parameter on
# instantiating a circle. Create a method to get area of the
# circle object.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # This is a method
        return (22/7) * self.radius ** 2

    def change_radius(self, radius):
        self.radius = radius


circle1 = Circle(4)  # This is an object instantiation
print(circle1.radius)
circle1.change_radius(10)
print(circle1.radius)
print(circle1.area())

circle2 = Circle(5)
print(circle2.area())

circle2.radius = 50
print(circle2.area())


# Characteristics of OOP
# 1. Inheritance  # Concept of parent and child classes
# 2. Encapsulation # protecting methods and properties
# 3. Polymorphism  # Different forms of same functions and methods
# 4. Abstraction   # Using methods and attributes of child class and not of the parent class

