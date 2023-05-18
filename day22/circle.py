class Circle:
    def __init__(self, radius):  # __init__
        self.radius = radius

    def total_radius(self, obj):
        return self.radius + obj.radius

    def __add__(self, obj):   # __add__
        return self.radius + obj.radius

    def __str__(self):   # str
        return "Circle object"

    def __gt__(self, other):  # __gt__
        if self.radius > other.radius:
            return True
        else:
            return False


c1 = Circle(10)
c2 = Circle(20)
print(c1)
total = c1.radius + c2.radius
print(total)

print(c1.total_radius(c2))
print(c1.__add__(c2))
print(c1 + c2)

if c1.radius > c2.radius:
    print("c1 is greater")
else:
    print("c2 is greater")

print(c2 < c1)
