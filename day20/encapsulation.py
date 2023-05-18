# Concept of making attributes private, public or protected

class Vehicle:
    def __init__(self, color, doors, mileage):
        self.color = color  # This is public attribute
        self._doors = doors  # These are protected attribute
        self.__mileage = mileage   # This is private attribute

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        if mileage > 60:
            self.__mileage = 60
        else:
            self.__mileage = mileage


# Public attributes can be changes from outside the class
car = Vehicle("blue", 4, 50)
print(car.color)   # Result => blue
car.color = 'red'
print(car.color)   # result => red


# Protected attributes can also be accessed from outside the class but not recommended
print(car._doors)
car._doors = 5
print(car._doors)


# Accessing private attributes outside the class is not possible
# print(car.__mileage)
# car.__mileage = 70

car.set_mileage(70)
print(car.get_mileage())


# But we can access private attributes from outside the class in some way
print(dir(car))
# On printing above line we can see '_Vehicle__mileage' attribute. So, we can access the private attributes
# from outside the class

print(car._Vehicle__mileage)   # This is also termed as name_mangling


# Dictionary Comprehension
a = [('name', "Jon"), ("age", 20), ("department", "CS")]
d = {k: v for k, v in a}
print(d)  # Result => {'name': 'Jon', 'age': 20, 'department': 'CS'}

d = {i: i for i in range(5)}
print(d)
