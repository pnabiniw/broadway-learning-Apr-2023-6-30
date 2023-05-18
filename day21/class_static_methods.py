from datetime import datetime
class Person:
    __age = 30

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def get_name(self):
        return self.name

    @classmethod
    def set_age(cls, age):
        cls.__age = age

    @classmethod
    def get_age(cls):
        return cls.__age


p = Person("Jon", "CS")
p.get_name()
Person.set_age(45)
print(Person.get_age())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):  # This is also called a factory method
        return cls(name, datetime.today().year-year)


a = Person("Jon", 25)
p = Person.from_birth_year("Jon", 1990)
print(p.age)


class Distance:
    def __init__(self, in_km):
        self.in_km = in_km

    @classmethod
    def from_miles(cls, miles):  # This is a factory method
        return cls(miles * 1.6)

    @staticmethod
    def message(d):
        if d < 20:
            return "It was a short distance"
        return "It was way too long !!"


d1 = Distance.from_miles(2)
print(d1.in_km)
