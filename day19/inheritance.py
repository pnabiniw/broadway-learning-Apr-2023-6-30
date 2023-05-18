class Vehicle:
    def __init__(self, capacity, doors):  # __init__
        self.seat_capacity = capacity
        self.doors = doors

    def get_vehicle_info(self):
        return f"The vehicle capacity is {self.seat_capacity} and it has {self.doors} doors"


class Car(Vehicle):   # This is single inheritance
    def __init__(self, capacity, doors, mileage, color):
        self.mileage = mileage  # This property is child specific
        self.color = color  # This property is also child specific
        super().__init__(capacity, doors)  # Common properties are assigned from the parent

    def get_vehicle_info(self):  # This method is overridden from parent class
        print(super().get_vehicle_info())
        return f"The car clor is {self.color} and it has {self.mileage}"


rover = Car(5, 4, 50, "blue")
print(rover.color)
rover.color = 'Blue'
print(rover.doors)
print(rover.mileage)
print(rover.seat_capacity)
print(rover.get_vehicle_info())
