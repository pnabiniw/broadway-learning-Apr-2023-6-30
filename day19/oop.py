class A:
    a = 10

    def __init__(self, b):  # This is a constructor
        self.b = b   # instance attribute

    def get_a(self):
        return self.a

    @classmethod
    def set_a(cls, a):
        cls.a = a

obj = A(5)
print(obj.a)
print(obj.b)
obj.get_a()

obj2 = A(10)

A.set_a(50)
print(obj.a)
print(obj2.a)
