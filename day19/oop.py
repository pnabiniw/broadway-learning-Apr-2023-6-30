class A:
    a = 10

    def __init__(self, b):  # This is a constructor
        self.b = b   # instance attribute

    def get_a(self):
        return self.a

obj = A(5)
print(obj.a)
print(obj.b)
obj.get_a()

