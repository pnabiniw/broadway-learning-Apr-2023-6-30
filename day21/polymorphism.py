def addition(a, b, c):
    return a + b


def addition(a, b, c):
    return a + b + c


# print(addition(2, 3))  # This gives error because function overloading
# is not possible in python
print(addition(2, 3, 4))


# We can give the feel of function overloading in following ways.
# But it is not actually the function overloading


def addition(a, b, c=5):
    return a + b + c


print(addition(2, 3))  # Call with two parameters
print(addition(2, 3, 7))  # Call with 3 parameters


def addition(*args):
    return sum(args)


# If *args is used then we can provide dynamic numbers of parameters
print(addition(2, 3))
print(addition(2, 3, 4))
print(addition(2, 3, 4, 5))


#  len() function is also one of the examples of polymorphism

print(len([1, 2, 3]))  # for list
print(len((1, 2, 3)))  # for tuple
print(len({1, 2, 3}))  # for set


# Method overloading example

class Shape:
    def area(self, l):
        return l * l

    def area(self, l, b=None):
        if not b:
            return l * l
        return l * b


# Method overloading is also not possible in python
square = Shape()
rectangle = Shape()
square.area(5)
rectangle.area(2, 3)


class Square(Shape):
    def area(self, l):
        return l * l


class Rectangle(Shape):
    def area(self, l, b):
        return l * b


square = Square()
print(square.area(5))
rectangle = Rectangle()
print(rectangle.area(2, 3))



class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name is {self.name} and age is {self.age}"


class Child(Parent):
    def __init__(self, name, age, faculty, batch):
        self.faculty = faculty
        self.batch = batch
        super().__init__(name, age)

    def get_info(self):
        print(super().get_info())
        print(self.name)
        print(self.age)
        return f"Faculty is {self.faculty} and batch is {self.batch}"


obj = Child("Jon", 25, "CS", 2080)
print(obj.get_info())
